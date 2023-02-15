# Results

- fork: iritkatriel
- ref: const_regs
- version: 3.12.0a4+
- commit hash: [80ea135](https://github.com/iritkatriel/cpython/commit/80ea135)
- commit date: 2023-01-16T23:41:38+00:00
- commit merge base: [762745a124cbc297cf2fe6f3ec9ca1840bb2e873](https://github.com/iritkatriel/cpython/commit/762745a124cbc297cf2fe6f3ec9ca1840bb2e873)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4%2B-80ea135.json)

### vs. 3.10.4

- 1.27x faster \*
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4%2B-80ea135-vs-3.10.4.md)
- [plot](bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4%2B-80ea135-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4%2B-80ea135-vs-3.11.0.md)
- [plot](bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4%2B-80ea135-vs-3.11.0.png)

### vs. base

- 1.02x slower
- [table](bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4%2B-80ea135-vs-base.md)
- [plot](bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4%2B-80ea135-vs-base.png)

