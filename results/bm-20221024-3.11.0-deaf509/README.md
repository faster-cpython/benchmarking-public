# Results

- fork: python
- version: 3.11.0
- commit hash: [deaf509](https://github.com/python/cpython/commit/deaf509)
- commit date: 2022-10-24T18:35:39+01:00
- ref: v3.11.0

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4950475325)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json)

### vs. 3.10.4

- 1.25x faster \*
- new benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md)
- [plot](bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4950475325)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json)

### vs. 3.10.4

- 1.21x faster \*
- new benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md)
- [plot](bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4950475325)
- cpu model: missing
- platform: Windows-10-10.0.22000-SP0
- [raw results](bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json)

### vs. 3.10.4

- 1.11x faster \*
- new benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md)
- [plot](bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4950475325)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: dask
- new benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md)
- [plot](bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.png)

