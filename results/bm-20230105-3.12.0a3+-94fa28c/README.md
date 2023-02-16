# Results

- fork: iritkatriel
- ref: InitializeHeader_noa
- version: 3.12.0a3+
- commit hash: [94fa28c](https://github.com/iritkatriel/cpython/commit/94fa28c)
- commit date: 2023-01-05T18:14:40+00:00
- commit merge base: [f20c553a458659f247fac1fb829f8172aa32f69a](https://github.com/iritkatriel/cpython/commit/f20c553a458659f247fac1fb829f8172aa32f69a)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3%2B-94fa28c.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3%2B-94fa28c-vs-3.10.4.md)
- [plot](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3%2B-94fa28c-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: djangocms
- [table](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3%2B-94fa28c-vs-3.11.0.md)
- [plot](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3%2B-94fa28c-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3%2B-94fa28c-vs-base.md)
- [plot](bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3%2B-94fa28c-vs-base.png)

