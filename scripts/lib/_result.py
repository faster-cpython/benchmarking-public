# Utilities to manage a results file


import functools
import json
from pathlib import Path
import subprocess


from lib import _git


def _clean(string):
    """
    Clean an arbitrary string to be suitable for a filename.

    It can't contain dashes, since dashes are used as a delimiter.
    """
    return string.replace("-", "_")


def _get_platform_value(python, item):
    """
    Get a value from the platform module of the given Python interpreter.
    """
    output = subprocess.check_output(
        [python, "-c", f"import platform; print(platform.{item}())"], encoding="utf-8"
    )
    return output.strip().lower()


class Comparison:
    def __init__(self, ref, head, base):
        self.ref = ref
        self.head = head
        self.base = base
        self._contents = None
        self._geometric_mean = None

    @property
    def geometric_mean(self):
        if self.ref == self.head:
            return ""

        if self._geometric_mean is None:
            contents = self.contents
            lines = list(contents.splitlines())

            if (
                self.head.benchmark_hash is None
                or self.ref.benchmark_hash != self.head.benchmark_hash
            ):
                suffix = r" \*"
            else:
                suffix = ""

            for line in lines:
                if "Geometric mean" in line:
                    self._geometric_mean = line.split("|")[3].strip() + suffix
                    break
            else:
                self._geometric_mean = "not sig"

        return self._geometric_mean

    @property
    def contents(self):
        if self._contents is None:
            if self.filename.with_suffix(".md").is_file():
                with open(
                    self.filename.with_suffix(".md"), "r", encoding="utf-8"
                ) as fd:
                    self._contents = fd.read()
            else:
                self._contents = subprocess.check_output(
                    [
                        "pyperf",
                        "compare_to",
                        "--table",
                        "--table-format",
                        "md",
                        self.ref.filename,
                        self.head.filename,
                    ],
                    encoding="utf-8",
                )
        return self._contents

    @property
    def filename(self):
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
        system,
        machine,
        fork,
        ref,
        version,
        cpython_hash,
        extra=[],
        suffix=".json",
        commit_datetime=None,
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
    def from_filename(cls, filename):
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
    def from_scratch(cls, python, fork, ref):
        return cls(
            _clean(_get_platform_value(python, "system")),
            _clean(_get_platform_value(python, "machine")),
            _clean(fork),
            _clean(ref[:20]),
            _clean(_get_platform_value(python, "python_version")),
            _git.get_git_hash("cpython")[:7],
            [],
            ".json",
        )

    @property
    def filename(self):
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
                        self.fork,
                        self.ref,
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
    def contents(self):
        with open(self.filename) as fd:
            return json.load(fd)

    @property
    def metadata(self):
        return self.contents.get("metadata", {})

    @property
    def commit_datetime(self):
        if self._commit_datetime is not None:
            return self._commit_datetime
        return self.metadata.get("commit_date", "<unknown>")

    @property
    def commit_date(self):
        return self.commit_datetime[:10]

    @property
    def commit_merge_base(self):
        return self.metadata.get("commit_merge_base", None)

    @property
    def benchmark_hash(self):
        return self.metadata.get("benchmark_hash", None)

    def match_to_bases(self, bases, results):
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


def load_all_results(bases, results_dir):
    results = []

    for entry in results_dir.glob("**/*.json"):
        results.append(Result.from_filename(entry))
    if len(results) == 0:
        raise ValueError("Didn't find any results.  That seems fishy.")

    for result in results:
        result.match_to_bases(bases, results)

    results.sort(key=lambda x: (x.version, x.commit_datetime))

    return results
