# Results

- fork: iritkatriel
- version: 3.12.0a3+
- commit hash: [e73d0cf](https://github.com/iritkatriel/cpython/commit/e73d0cf)
- commit date: 2023-01-04T22:39:29+00:00
- commit merge base: [64ed609c532a12b27f67a1e12e9e02f136ee3a94](https://github.com/iritkatriel/cpython/commit/64ed609c532a12b27f67a1e12e9e02f136ee3a94)
- ref: InitializeHeader

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-e73d0cf.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-e73d0cf-vs-3.10.4.md)
- [plot](bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-e73d0cf-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-e73d0cf-vs-3.11.0.md)
- [plot](bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-e73d0cf-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-e73d0cf-vs-base.md)
- [plot](bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-e73d0cf-vs-base.png)

