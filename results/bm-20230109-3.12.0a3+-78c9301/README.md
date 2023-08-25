# Results

- fork: Fidget_Spinner
- version: 3.12.0a3+
- commit hash: [78c9301](https://github.com/Fidget_Spinner/cpython/commit/78c9301)
- commit date: 2023-01-09T12:55:54+08:00
- commit merge base: [7116030a25f7dd2140ef3e889f3f5471334d6d0b](https://github.com/Fidget_Spinner/cpython/commit/7116030a25f7dd2140ef3e889f3f5471334d6d0b)
- ref: per_class_cache

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3%2B-78c9301.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster \* (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3%2B-78c9301-vs-3.10.4.md)
- [plot](bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3%2B-78c9301-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster \* (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3%2B-78c9301-vs-3.11.0.md)
- [plot](bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3%2B-78c9301-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- [table](bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3%2B-78c9301-vs-base.md)
- [plot](bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3%2B-78c9301-vs-base.png)

