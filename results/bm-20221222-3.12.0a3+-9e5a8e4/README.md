# Results

- fork: brandtbucher
- version: 3.12.0a3+
- commit hash: [9e5a8e4](https://github.com/brandtbucher/cpython/commit/9e5a8e4)
- commit date: 2022-12-22T21:48:09-08:00
- commit merge base: [3c033a2e6fbde56f904aeca138141be6564341cf](https://github.com/brandtbucher/cpython/commit/3c033a2e6fbde56f904aeca138141be6564341cf)
- ref: scan_small_dicts

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-9e5a8e4.json)

### vs. 3.10.4

- 1.29x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-9e5a8e4-vs-3.10.4.md)
- [plot](bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-9e5a8e4-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-9e5a8e4-vs-3.11.0.md)
- [plot](bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-9e5a8e4-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-9e5a8e4-vs-base.md)
- [plot](bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-9e5a8e4-vs-base.png)

