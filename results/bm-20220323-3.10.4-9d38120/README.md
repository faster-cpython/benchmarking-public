# Results

- fork: python
- version: 3.10.4
- commit hash: [9d38120](https://github.com/python/cpython/commit/9d38120)
- commit date: 2022-03-23T20:12:04+00:00
- ref: 9d38120e335357a3b294, v3.10.4

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4511521606)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json)

### vs. 3.11.0

- 1.25x slower \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.md)
- [plot](bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4543286920)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.11.0

- 1.22x slower \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md)
- [plot](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4491158802)
- cpu model: missing
- platform: Windows-10-10.0.22000-SP0
- [raw results](bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json)

### vs. 3.11.0

- 1.11x slower \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.md)
- [plot](bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4491167090)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.11.0

- 1.21x slower \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md)
- [plot](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.png)

