# Results

- fork: brandtbucher
- ref: scan_small_dicts
- version: 3.12.0a3+
- commit hash: [ba16621](https://github.com/brandtbucher/cpython/commit/ba16621)
- commit date: 2022-12-17T13:59:40-08:00
- commit merge base: [3c033a2e6fbde56f904aeca138141be6564341cf](https://github.com/brandtbucher/cpython/commit/3c033a2e6fbde56f904aeca138141be6564341cf)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-ba16621.json)

### vs. 3.10.4

- 1.31x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-ba16621-vs-3.10.4.md)
- [plot](bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-ba16621-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-ba16621-vs-3.11.0.md)
- [plot](bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-ba16621-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-ba16621-vs-base.md)
- [plot](bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3%2B-ba16621-vs-base.png)

