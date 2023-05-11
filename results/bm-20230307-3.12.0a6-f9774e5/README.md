# Results

- fork: python
- version: 3.12.0a6
- commit hash: [f9774e5](https://github.com/python/cpython/commit/f9774e5)
- commit date: 2023-03-07T22:48:18+01:00
- ref: f9774e57d84162ff0cba

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4546447152)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230307-linux-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5.json)

### vs. 3.10.4

- 1.29x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230307-linux-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.md)
- [plot](bm-20230307-linux-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230307-linux-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.md)
- [plot](bm-20230307-linux-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4546461484)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5.json)

### vs. 3.10.4

- 1.27x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.md)
- [plot](bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.md)
- [plot](bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4511434980)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5.json)

### vs. 3.10.4

- 1.20x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.md)
- [plot](bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.png)

### vs. 3.11.0

- 1.09x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.md)
- [plot](bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4546451869)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5.json)

### vs. 3.10.4

- 1.19x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.md)
- [plot](bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.md)
- [plot](bm-20230307-darwin-arm64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5-vs-3.11.0.png)

