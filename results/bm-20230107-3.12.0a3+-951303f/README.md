# Results

- fork: python
- version: 3.12.0a3+
- commit hash: [951303f](https://github.com/python/cpython/commit/951303f)
- commit date: 2023-01-07T21:29:53+00:00
- ref: main

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230107-linux-x86_64-python-main-3.12.0a3%2B-951303f-pystats.json)
- [pystats table](bm-20230107-linux-x86_64-python-main-3.12.0a3%2B-951303f-pystats.md)
- [raw results](bm-20230107-linux-x86_64-python-main-3.12.0a3%2B-951303f.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230107-linux-x86_64-python-main-3.12.0a3%2B-951303f-vs-3.10.4.md)
- [plot](bm-20230107-linux-x86_64-python-main-3.12.0a3%2B-951303f-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230107-linux-x86_64-python-main-3.12.0a3%2B-951303f-vs-3.11.0.md)
- [plot](bm-20230107-linux-x86_64-python-main-3.12.0a3%2B-951303f-vs-3.11.0.png)

## darwin arm64 (darwin)

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20230107-darwin-arm64-python-main-3.12.0a3%2B-951303f.json)

### vs. 3.10.4

- 1.24x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230107-darwin-arm64-python-main-3.12.0a3%2B-951303f-vs-3.10.4.md)
- [plot](bm-20230107-darwin-arm64-python-main-3.12.0a3%2B-951303f-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230107-darwin-arm64-python-main-3.12.0a3%2B-951303f-vs-3.11.0.md)
- [plot](bm-20230107-darwin-arm64-python-main-3.12.0a3%2B-951303f-vs-3.11.0.png)

