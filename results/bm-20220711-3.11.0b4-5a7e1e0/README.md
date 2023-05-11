# Results

- fork: python
- version: 3.11.0b4
- commit hash: [5a7e1e0](https://github.com/python/cpython/commit/5a7e1e0)
- commit date: 2022-07-11T16:25:22+01:00
- ref: 5a7e1e0a92622c605ab2

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20220711-linux-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0.json)

### vs. 3.10.4

- 1.29x faster \*
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, comprehensions, coverage, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20220711-linux-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.md)
- [plot](bm-20220711-linux-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, comprehensions, coverage, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20220711-linux-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.md)
- [plot](bm-20220711-linux-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513536147)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20220711-pythonperf2-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0.json)

### vs. 3.10.4

- 1.22x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220711-pythonperf2-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.md)
- [plot](bm-20220711-pythonperf2-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220711-pythonperf2-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.md)
- [plot](bm-20220711-pythonperf2-x86_64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4483411326)
- cpu model: missing
- platform: Windows-10-10.0.22000-SP0
- [raw results](bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0.json)

### vs. 3.10.4

- 1.10x faster \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.md)
- [plot](bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.md)
- [plot](bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494503936)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20220711-darwin-arm64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0.json)

### vs. 3.10.4

- 1.20x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220711-darwin-arm64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.md)
- [plot](bm-20220711-darwin-arm64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20220711-darwin-arm64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.md)
- [plot](bm-20220711-darwin-arm64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0-vs-3.11.0.png)

