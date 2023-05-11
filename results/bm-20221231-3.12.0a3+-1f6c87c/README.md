# Results

- fork: python
- version: 3.12.0a3+
- commit hash: [1f6c87c](https://github.com/python/cpython/commit/1f6c87c)
- commit date: 2022-12-31T19:01:44-05:00
- ref: main

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20221231-linux-x86_64-python-main-3.12.0a3%2B-1f6c87c-pystats.json)
- [pystats table](bm-20221231-linux-x86_64-python-main-3.12.0a3%2B-1f6c87c-pystats.md)
- [raw results](bm-20221231-linux-x86_64-python-main-3.12.0a3%2B-1f6c87c.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20221231-linux-x86_64-python-main-3.12.0a3%2B-1f6c87c-vs-3.10.4.md)
- [plot](bm-20221231-linux-x86_64-python-main-3.12.0a3%2B-1f6c87c-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221231-linux-x86_64-python-main-3.12.0a3%2B-1f6c87c-vs-3.11.0.md)
- [plot](bm-20221231-linux-x86_64-python-main-3.12.0a3%2B-1f6c87c-vs-3.11.0.png)

