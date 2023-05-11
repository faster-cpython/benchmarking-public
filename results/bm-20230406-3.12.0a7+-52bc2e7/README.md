# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [52bc2e7](https://github.com/python/cpython/commit/52bc2e7)
- commit date: 2023-04-06T14:05:23+01:00
- ref: 52bc2e7b9d451821513a

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4634397966)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7.json)

### vs. 3.10.4

- 1.31x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.md)
- [plot](bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.md)
- [plot](bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4672599617)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7.json)

### vs. 3.10.4

- 1.20x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.md)
- [plot](bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.png)

### vs. 3.11.0

- 1.08x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.md)
- [plot](bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4801195541)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7.json)

### vs. 3.10.4

- 1.20x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.md)
- [plot](bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.md)
- [plot](bm-20230406-darwin-arm64-python-52bc2e7b9d451821513a-3.12.0a7%2B-52bc2e7-vs-3.11.0.png)

