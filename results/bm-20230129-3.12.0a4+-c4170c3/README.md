# Results

- fork: python
- version: 3.12.0a4+
- commit hash: [c4170c3](https://github.com/python/cpython/commit/c4170c3)
- commit date: 2023-01-29T16:41:27-08:00
- ref: c4170c36b0b54c10456f

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513537722)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230129-pythonperf2-x86_64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3.json)

### vs. 3.10.4

- 1.27x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230129-pythonperf2-x86_64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.10.4.md)
- [plot](bm-20230129-pythonperf2-x86_64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230129-pythonperf2-x86_64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.11.0.md)
- [plot](bm-20230129-pythonperf2-x86_64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610450893)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.10.4.md)
- [plot](bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.10.4.png)

### vs. 3.11.0

- 1.10x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.11.0.md)
- [plot](bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494505524)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230129-darwin-arm64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3.json)

### vs. 3.10.4

- 1.22x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230129-darwin-arm64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.10.4.md)
- [plot](bm-20230129-darwin-arm64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230129-darwin-arm64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.11.0.md)
- [plot](bm-20230129-darwin-arm64-python-c4170c36b0b54c10456f-3.12.0a4%2B-c4170c3-vs-3.11.0.png)

