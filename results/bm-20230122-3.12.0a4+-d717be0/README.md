# Results

- fork: python
- version: 3.12.0a4+
- commit hash: [d717be0](https://github.com/python/cpython/commit/d717be0)
- commit date: 2023-01-22T17:16:48-08:00
- ref: d717be04dc7876696cb2

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513537625)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230122-pythonperf2-x86_64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230122-pythonperf2-x86_64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.10.4.md)
- [plot](bm-20230122-pythonperf2-x86_64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230122-pythonperf2-x86_64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.11.0.md)
- [plot](bm-20230122-pythonperf2-x86_64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610450851)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.10.4.md)
- [plot](bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.10.4.png)

### vs. 3.11.0

- 1.09x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.11.0.md)
- [plot](bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494505395)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230122-darwin-arm64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230122-darwin-arm64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.10.4.md)
- [plot](bm-20230122-darwin-arm64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230122-darwin-arm64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.11.0.md)
- [plot](bm-20230122-darwin-arm64-python-d717be04dc7876696cb2-3.12.0a4%2B-d717be0-vs-3.11.0.png)

