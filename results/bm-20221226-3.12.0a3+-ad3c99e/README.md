# Results

- fork: python
- version: 3.12.0a3+
- commit hash: [ad3c99e](https://github.com/python/cpython/commit/ad3c99e)
- commit date: 2022-12-26T00:22:53-06:00
- ref: ad3c99e521151680afc6

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513537311)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20221226-pythonperf2-x86_64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e.json)

### vs. 3.10.4

- 1.26x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221226-pythonperf2-x86_64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.10.4.md)
- [plot](bm-20221226-pythonperf2-x86_64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221226-pythonperf2-x86_64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.11.0.md)
- [plot](bm-20221226-pythonperf2-x86_64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610450607)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e.json)

### vs. 3.10.4

- 1.16x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.10.4.md)
- [plot](bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.10.4.png)

### vs. 3.11.0

- 1.05x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.11.0.md)
- [plot](bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494505019)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20221226-darwin-arm64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221226-darwin-arm64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.10.4.md)
- [plot](bm-20221226-darwin-arm64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20221226-darwin-arm64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.11.0.md)
- [plot](bm-20221226-darwin-arm64-python-ad3c99e521151680afc6-3.12.0a3%2B-ad3c99e-vs-3.11.0.png)

