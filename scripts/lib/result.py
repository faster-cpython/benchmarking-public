# Utilities to manage a results file


import functools
import json
from pathlib import Path
import subprocess
from typing import Any, Dict, Iterable, List, Optional


from packaging import version as pkg_version


from lib import git


def _clean(string: str) -> str:
    """
    Clean an arbitrary string to be suitable for a filename.

    It can't contain dashes, since dashes are used as a delimiter.
    """
    return string.replace("-", "_")


def _clean_for_url(string: str) -> str:
    """
    Clean an arbitrary string to be suitable for a filename, being careful to
    create something that can be re-used as a URL.

    It can't contain dashes, since dashes are used as a delimiter.
    """
    return string.replace("-", "%2d")


def _get_platform_value(python: str, item: str) -> str:
    """
    Get a value from the platform module of the given Python interpreter.
    """
    output = subprocess.check_output(
        [python, "-c", f"import platform; print(platform.{item}())"], encoding="utf-8"
    )
    return output.strip().lower()


class Comparison:
    def __init__(self, ref: "Result", head: "Result", base: str):
        self.ref = ref
        self.head = head
        self.base = base

    def copy(self):
        return type(self)(self.ref, self.head, self.base)

    @property
    @functools.cache
    def geometric_mean(self) -> str:
        if self.ref == self.head:
            return ""

        contents = self.contents
        if contents is None:
            return ""

        lines = list(contents.splitlines())

        if (
            self.head.benchmark_hash is None
            or self.ref.benchmark_hash != self.head.benchmark_hash
        ):
            suffix = r" \*"
        else:
            suffix = ""

        geometric_mean = None
        for line in lines:
            # We want to get the *last* geometric mean in the file, in case
            # it's divided by tags
            if "Geometric mean" in line:
                geometric_mean = line.split("|")[3].strip() + suffix

        if geometric_mean is None:
            geometric_mean = "not sig"

        return geometric_mean

    @property
    def geometric_mean_float(self) -> float:
        parts = self.geometric_mean.split(" ")
        if len(parts) == 1:
            return 1.0
        (number, direction, *_) = parts
        number = float(number[:-1])
        if direction == "slower":
            number = 1.0 - (number - 1.0)
        return number

    @property
    @functools.cache
    def contents(self) -> Optional[str]:
        if self.filename is None:
            return None

        if self.filename.with_suffix(".md").is_file():
            with open(self.filename.with_suffix(".md"), "r", encoding="utf-8") as fd:
                return fd.read()
        else:
            return subprocess.check_output(
                [
                    "pyperf",
                    "compare_to",
                    "-G",
                    "--table",
                    "--table-format",
                    "md",
                    self.ref.filename,
                    self.head.filename,
                ],
                encoding="utf-8",
            )

    @property
    def filename(self) -> Optional[Path]:
        if self.ref == self.head:
            return None

        return self.head.filename.parent / (
            self.head.filename.stem + f"-vs-{self.base}.txt"
        )


class Result:
    """
    Stores information about a single result file.
    """

    def __init__(
        self,
        system: str,
        machine: str,
        fork: str,
        ref: str,
        version: str,
        cpython_hash: str,
        extra: List[str] = [],
        suffix: str = ".json",
        commit_datetime: Optional[str] = None,
    ):
        self.system = system
        self.machine = machine
        self.fork = fork
        self.ref = ref
        self.version = version
        self.cpython_hash = cpython_hash
        self.extra = extra
        self.suffix = suffix
        self._commit_datetime = commit_datetime
        self._filename = None
        self.bases = {}

    @classmethod
    def from_filename(cls, filename: Path) -> "Result":
        (
            name,
            date,
            system,
            machine,
            fork,
            ref,
            version,
            cpython_hash,
            *extra,
        ) = filename.stem.split("-")
        assert name == "bm"
        obj = cls(
            system=system,
            machine=machine,
            fork=fork,
            ref=ref,
            version=version,
            cpython_hash=cpython_hash,
            extra=extra,
            suffix=filename.suffix,
        )
        obj._filename = filename
        return obj

    @classmethod
    def from_scratch(
        cls, python: str, fork: str, ref: str, extra: List[str] = []
    ) -> "Result":
        result = cls(
            _clean(_get_platform_value(python, "system")),
            _clean(_get_platform_value(python, "machine")),
            _clean_for_url(fork),
            _clean(ref[:20]),
            _clean(_get_platform_value(python, "python_version")),
            git.get_git_hash("cpython")[:7],
            extra,
            ".json",
            commit_datetime=git.get_git_commit_date("cpython"),
        )
        return result

    @property
    def filename(self) -> Path:
        if self._filename is None:
            date = self.commit_date.replace("-", "")
            if self.extra:
                extra = ["-".join(self.extra)]
            else:
                extra = []
            self._filename = (
                Path("results")
                / "-".join(
                    [
                        "bm",
                        date,
                        self.version,
                        self.cpython_hash,
                    ]
                )
                / (
                    "-".join(
                        [
                            "bm",
                            date,
                            self.system,
                            self.machine,
                            self.fork,
                            self.ref,
                            self.version,
                            self.cpython_hash,
                        ]
                        + extra
                    )
                    + self.suffix
                )
            )
        return self._filename

    @property
    @functools.cache
    def result_type(self) -> str:
        """
        Get a human-readable description of the result type.
        """
        if self.extra == [] and self.suffix == ".json":
            return "raw results"
        elif self.extra == ["pystats"]:
            if self.suffix == ".md":
                return "pystats table"
            elif self.suffix == ".json":
                return "pystats raw data"
        elif len(self.extra) == 2 and self.extra[0] == "vs":
            if self.suffix == ".md":
                return f"table vs. {self.extra[1]}"
            elif self.suffix == ".png":
                return f"plot vs. {self.extra[1]}"
        raise ValueError("Unknown result type")

    @property
    @functools.cache
    def contents(self) -> Dict[str, Any]:
        with open(self.filename) as fd:
            return json.load(fd)

    @property
    def metadata(self) -> Dict[str, Any]:
        return self.contents.get("metadata", {})

    @property
    def commit_datetime(self) -> str:
        if self._commit_datetime is not None:
            return self._commit_datetime
        return self.metadata.get("commit_date", "<unknown>")

    @property
    def commit_date(self) -> str:
        return self.commit_datetime[:10]

    @property
    def commit_merge_base(self) -> str:
        return self.metadata.get("commit_merge_base", None)

    @property
    def benchmark_hash(self) -> str:
        return self.metadata.get("benchmark_hash", None)

    @property
    @functools.cache
    def parsed_version(self) -> pkg_version.Version:
        return pkg_version.parse(self.version.replace("+", "0"))

    def match_to_bases(self, bases: List[str], results: Iterable["Result"]) -> None:
        loose_results = [
            ref
            for ref in results
            if ref != self
            and ref.system == self.system
            and ref.machine == self.machine
            and ref.fork == "python"
        ]

        if self.benchmark_hash is not None:
            exact_results = [
                ref
                for ref in loose_results
                if ref.benchmark_hash == self.benchmark_hash
            ]
        else:
            exact_results = []

        def find_match(base, func):
            # Try for an exact match (same benchmark_hash) first,
            # then fall back to less exact.
            for ref in exact_results:
                if func(ref):
                    self.bases[base] = Comparison(ref, self, base)
                    break
            else:
                for ref in loose_results:
                    if func(ref):
                        self.bases[base] = Comparison(ref, self, base)
                        break

        for base in bases:
            find_match(base, lambda ref: ref.version == base)

        merge_base = self.commit_merge_base
        if merge_base is not None:
            find_match("base", lambda ref: merge_base.startswith(ref.cpython_hash))


def load_all_results(bases: List[str], results_dir: Path) -> List[Result]:
    results = []

    for entry in results_dir.glob("**/*.json"):
        result = Result.from_filename(entry)
        if not result.result_type == "raw results":
            continue
        results.append(Result.from_filename(entry))
    if len(results) == 0:
        raise ValueError("Didn't find any results.  That seems fishy.")

    for result in results:
        result.match_to_bases(bases, results)

    results.sort(
        key=lambda x: (
            x.parsed_version,
            x.commit_datetime,
        ),
        reverse=True,
    )

    return results
