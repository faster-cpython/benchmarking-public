# Utilities to manage a results file


import functools
import json
from pathlib import Path
import socket
import subprocess
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


from lib import git
from lib import runners


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

    @functools.cached_property
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
        geometric_mean = self.geometric_mean
        if geometric_mean == "not sig":
            return 1.0
        parts = geometric_mean.split(" ")
        if len(parts) == 1:
            return 1.0
        (number, direction, *_) = parts
        number = float(number[:-1])
        if direction == "slower":
            number = 1.0 - (number - 1.0)
        return number

    @functools.cached_property
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
        nickname: str,
        machine: str,
        fork: str,
        ref: str,
        version: str,
        cpython_hash: str,
        extra: List[str] = [],
        suffix: str = ".json",
        commit_datetime: Optional[str] = None,
    ):
        self.nickname = nickname
        if nickname not in runners.RUNNERS_BY_NICKNAME:
            raise ValueError(f"Unknown runner {nickname}")
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
            nickname,
            machine,
            fork,
            ref,
            version,
            cpython_hash,
            *extra,
        ) = filename.stem.split("-")
        assert name == "bm"
        obj = cls(
            nickname=nickname,
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
            _clean(runners.get_nickname_for_hostname(socket.gethostname())),
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
                            self.nickname,
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

    @functools.cached_property
    def result_info(self) -> Tuple[str, Optional[str]]:
        if self.extra == [] and self.suffix == ".json":
            return ("raw results", None)
        elif self.extra == ["pystats"]:
            if self.suffix == ".md":
                return ("pystats table", None)
            elif self.suffix == ".json":
                return ("pystats raw", None)
        elif len(self.extra) == 2 and self.extra[0] == "vs":
            if self.suffix == ".md":
                return ("table", self.extra[1])
            elif self.suffix == ".png":
                return ("plot", self.extra[1])
        raise ValueError("Unknown result type")

    @property
    def fast_contents(self) -> Dict[str, Any]:
        """
        Gets just a portion of the JSON contents when the whole set isn't needed.
        """
        if hasattr(self, "_full_contents"):
            return self._full_contents
        if hasattr(self, "_fast_contents"):
            return self._fast_contents

        try:
            import ijson
        except ImportError:
            return self.contents

        fast_contents = {"metadata": {}, "benchmarks": []}
        with open(self.filename, "rb") as fd:
            parser = ijson.parse(fd)
            for prefix, _, value in parser:
                if prefix == "benchmarks.item.metadata.name":
                    fast_contents["benchmarks"].append({"metadata": {"name": value}})
                elif prefix == "benchmarks.item.runs.item.metadata.date":
                    if len(fast_contents["benchmarks"]) == 0:
                        fast_contents["benchmarks"].append({})
                    if len(fast_contents["benchmarks"]) == 1:
                        fast_contents["benchmarks"][-1]["runs"] = [
                            {"metadata": {"date": value}}
                        ]
                elif prefix.startswith("metadata."):
                    fast_contents["metadata"][prefix[9:]] = value

        self._fast_contents = fast_contents
        return fast_contents

    @property
    def contents(self) -> Dict[str, Any]:
        if hasattr(self, "_full_contents"):
            return self._full_contents
        with open(self.filename, "rb") as fd:
            self._full_contents = json.load(fd)
        return self._full_contents

    @property
    def metadata(self) -> Dict[str, Any]:
        return self.fast_contents.get("metadata", {})

    @property
    def commit_datetime(self) -> str:
        if self._commit_datetime is not None:
            return self._commit_datetime
        return self.metadata.get("commit_date", "<unknown>")

    @property
    def commit_date(self) -> str:
        return self.commit_datetime[:10]

    @property
    def run_datetime(self) -> str:
        return self.fast_contents["benchmarks"][0]["runs"][0]["metadata"]["date"]

    @property
    def run_date(self) -> str:
        return self.run_datetime[:10]

    @property
    def commit_merge_base(self) -> str:
        return self.metadata.get("commit_merge_base", None)

    @property
    def benchmark_hash(self) -> str:
        return self.metadata.get("benchmark_hash", None)

    @property
    def hostname(self) -> str:
        return self.metadata.get("hostname", "unknown host")

    @property
    def system(self) -> str:
        return runners.get_runner_by_nickname(self.nickname).os

    @property
    def runner(self) -> str:
        return f"{self.system} {self.machine} ({self.nickname})"

    @property
    def cpu_model_name(self) -> str:
        return self.metadata.get("cpu_model_name", "missing")

    @property
    def platform(self) -> str:
        return self.metadata.get("platform", "missing")

    @property
    def github_action_url(self) -> Optional[str]:
        return self.metadata.get("github_action_url", None)

    @functools.cached_property
    def benchmark_names(self) -> Set[str]:
        contents = self.fast_contents
        names = set()
        for benchmark in contents["benchmarks"]:
            if "metadata" in benchmark:
                names.add(benchmark["metadata"]["name"])
            else:
                names.add(contents["metadata"]["name"])
        return names

    @functools.cached_property
    def parsed_version(self):
        from packaging import version as pkg_version

        return pkg_version.parse(self.version.replace("+", "0"))

    def match_to_bases(self, bases: List[str], results: Iterable["Result"]) -> None:
        loose_results = [
            ref
            for ref in results
            if ref != self and ref.nickname == self.nickname and ref.fork == "python"
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
            for result_set in [exact_results, loose_results]:
                for ref in result_set:
                    if func(ref):
                        self.bases[base] = Comparison(ref, self, base)
                        return

        for base in bases:
            find_match(base, lambda ref: ref.version == base)

        merge_base = self.commit_merge_base
        if merge_base is not None:
            find_match("base", lambda ref: merge_base.startswith(ref.cpython_hash))


def remove_duplicate_results(results_dir: Path) -> None:
    sifted = {}
    for entry in results_dir.glob("**/*.json"):
        result = Result.from_filename(entry)
        if result.result_info != ("raw results", None):
            continue
        result = Result.from_filename(entry)
        key = (result.nickname, result.cpython_hash, result.result_info)
        sifted.setdefault(key, []).append(result)

    for result_set in sifted.values():
        if len(result_set) != 1:
            result_set.sort(key=lambda x: x.run_datetime)
            for result in result_set[:-1]:
                result.filename.unlink()


def has_result(results_dir: Path, commit_hash: str, machine: str) -> Optional[Result]:
    if machine == "all":
        nickname = None
    else:
        _, _, nickname = machine.split("-")

    for result in load_all_results([], results_dir, False):
        if commit_hash.startswith(result.cpython_hash) and (
            nickname is None or result.nickname == nickname
        ):
            return result

    return None


def load_all_results(
    bases: Optional[List[str]], results_dir: Path, sorted: bool = True
) -> List[Result]:
    results = []

    for entry in results_dir.glob("**/*.json"):
        result = Result.from_filename(entry)
        if result.result_info != ("raw results", None):
            continue
        results.append(Result.from_filename(entry))
    if len(results) == 0:
        raise ValueError("Didn't find any results.  That seems fishy.")

    if bases is not None:
        for result in results:
            result.match_to_bases(bases, results)

    if sorted:
        results.sort(
            key=lambda x: (
                x.parsed_version,
                x.commit_datetime,
            ),
            reverse=True,
        )

    return results
