# Results

- fork: python
- ref: 594de165bf2f21d6b28e
- version: 3.12.0a2+
- commit hash: [594de16](https://github.com/python/cpython/commit/594de16)
- commit date: 2022-11-28T01:49:10-05:00

## darwin arm64

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16.json)

### vs. 3.10.4

- 1.19x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.md)
- [plot](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x slower
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.md)
- [plot](bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.png)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16.json)

### vs. 3.10.4

- 1.31x faster \*
- missing benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.md)
- [plot](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.md)
- [plot](bm-20221128-linux-x86_64-python-594de165bf2f21d6b28e-3.12.0a2%2B-594de16-vs-3.11.0.png)

