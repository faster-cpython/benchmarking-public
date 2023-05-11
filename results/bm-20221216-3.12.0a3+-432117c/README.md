# Results

- fork: python
- version: 3.12.0a3+
- commit hash: [432117c](https://github.com/python/cpython/commit/432117c)
- commit date: 2022-12-16T12:36:13-08:00
- ref: main

## darwin arm64 (darwin)

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20221216-darwin-arm64-python-main-3.12.0a3%2B-432117c.json)

### vs. 3.10.4

- 1.25x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20221216-darwin-arm64-python-main-3.12.0a3%2B-432117c-vs-3.10.4.md)
- [plot](bm-20221216-darwin-arm64-python-main-3.12.0a3%2B-432117c-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221216-darwin-arm64-python-main-3.12.0a3%2B-432117c-vs-3.11.0.md)
- [plot](bm-20221216-darwin-arm64-python-main-3.12.0a3%2B-432117c-vs-3.11.0.png)

