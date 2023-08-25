# Results

- fork: iritkatriel
- version: 3.12.0a3+
- commit hash: [d501577](https://github.com/iritkatriel/cpython/commit/d501577)
- commit date: 2023-01-05T13:09:34+00:00
- commit merge base: [f20c553a458659f247fac1fb829f8172aa32f69a](https://github.com/iritkatriel/cpython/commit/f20c553a458659f247fac1fb829f8172aa32f69a)
- ref: InitializeHeader

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-d501577.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-d501577-vs-3.10.4.md)
- [plot](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-d501577-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-d501577-vs-3.11.0.md)
- [plot](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-d501577-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 97.10%, 1.00x slower at 99th %ile)
- [table](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-d501577-vs-base.md)
- [plot](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3%2B-d501577-vs-base.png)

