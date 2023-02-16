# Results

- fork: pablogsal
- ref: gc_nogen
- version: 3.12.0a3+
- commit hash: [663a965](https://github.com/pablogsal/cpython/commit/663a965)
- commit date: 2022-12-21T14:11:06+00:00
- commit merge base: [a7715ccfba5b86ab09f86ec56ac3755c93b46b48](https://github.com/pablogsal/cpython/commit/a7715ccfba5b86ab09f86ec56ac3755c93b46b48)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3%2B-663a965.json)

### vs. 3.10.4

- 1.37x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy
- [table](bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3%2B-663a965-vs-3.10.4.md)
- [plot](bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3%2B-663a965-vs-3.10.4.png)

### vs. 3.11.0

- 1.08x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [table](bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3%2B-663a965-vs-3.11.0.md)
- [plot](bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3%2B-663a965-vs-3.11.0.png)

### vs. base

- 1.05x faster
- [table](bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3%2B-663a965-vs-base.md)
- [plot](bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3%2B-663a965-vs-base.png)

