# Results

- fork: python
- version: 3.11.0rc2
- commit hash: [ed7c3ff](https://github.com/python/cpython/commit/ed7c3ff)
- commit date: 2022-09-11T20:23:30+01:00
- ref: ed7c3ff15680c1939fad

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20220911-linux-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff.json)

### vs. 3.10.4

- 1.27x faster \*
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, comprehensions, coverage, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20220911-linux-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.md)
- [plot](bm-20220911-linux-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x slower \*
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, comprehensions, coverage, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20220911-linux-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.md)
- [plot](bm-20220911-linux-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513536491)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.md)
- [plot](bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.md)
- [plot](bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4483411552)
- cpu model: missing
- platform: Windows-10-10.0.22000-SP0
- [raw results](bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff.json)

### vs. 3.10.4

- 1.11x faster \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.md)
- [plot](bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.md)
- [plot](bm-20220911-pythonperf1-amd64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494504204)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.md)
- [plot](bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.md)
- [plot](bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff-vs-3.11.0.png)

