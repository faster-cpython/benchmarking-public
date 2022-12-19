"""
Utilities to use the `gh` CLI for workflow automation.
"""

from pathlib import Path
import subprocess
from typing import Any, List, Mapping, Optional


def _get_flags(d: Mapping[str, Any]) -> List[str]:
    flags = []
    for key, val in d.items():
        if val is None:
            continue
        if isinstance(val, bool):
            val = str(val).lower()
        else:
            val = str(val)
        flags.extend(["-f", f"{key}={val}"])
    return flags


MACHINES = ["linux-amd64", "windows-amd64", "darwin-arm64", "all"]


def benchmark(
    fork: Optional[str] = None,
    ref: Optional[str] = None,
    machine: Optional[str] = None,
    benchmark_base: Optional[str] = None,
    publish: Optional[str] = None,
) -> None:
    if not (fork is None or isinstance(fork, str)):
        raise TypeError(f"fork must be a str, got {type(fork)}")

    if not (ref is None or isinstance(ref, str)):
        raise TypeError(f"ref must be a str, got {type(ref)}")

    if not (machine is None or machine in MACHINES):
        raise ValueError(f"machine must be one of {MACHINES}")

    if not (benchmark_base is None or isinstance(benchmark_base, bool)):
        raise TypeError(f"benchmark_base must be bool, got {type(benchmark_base)}")

    if not (publish is None or isinstance(publish, bool)):
        raise TypeError(f"publish must be bool, got {type(publish)}")

    flags = _get_flags(
        {
            "fork": fork,
            "ref": ref,
            "machine": machine,
            "benchmark_base": benchmark_base,
            "publish": publish,
        }
    )

    subprocess.check_call(
        ["gh", "workflow", "run", "benchmark.yml"] + flags,
        cwd=Path(__file__).parents[1],
    )
