import subprocess


import pytest


from scripts.lib import gh


def test_benchmark_arguments():
    with pytest.raises(TypeError):
        gh.benchmark(fork=1)

    with pytest.raises(TypeError):
        gh.benchmark(ref=1)

    with pytest.raises(ValueError):
        gh.benchmark(machine="")

    with pytest.raises(ValueError):
        gh.benchmark(machine="linux-x86_64")

    with pytest.raises(TypeError):
        gh.benchmark(benchmark_base=1)

    with pytest.raises(TypeError):
        gh.benchmark(publish=1)


def test_benchmark_cmdline(monkeypatch):
    args_out = None

    def get_args(args, **kwargs):
        nonlocal args_out
        args_out = args

    monkeypatch.setattr(subprocess, "check_call", get_args)

    gh.benchmark(fork="myfork", benchmark_base=True)

    assert args_out == [
        "gh",
        "workflow",
        "run",
        "benchmark.yml",
        "-f",
        "fork=myfork",
        "-f",
        "benchmark_base=true",
    ]
