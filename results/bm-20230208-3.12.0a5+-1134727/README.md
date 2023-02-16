# Results

- fork: iritkatriel
- ref: int_freelist
- version: 3.12.0a5+
- commit hash: [1134727](https://github.com/iritkatriel/cpython/commit/1134727)
- commit date: 2023-02-08T18:26:54+00:00
- commit merge base: [d9de0792482d2ded364b0c7d2867b97a5da41b12](https://github.com/iritkatriel/cpython/commit/d9de0792482d2ded364b0c7d2867b97a5da41b12)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: dask, flaskblogging, pylint
- [table](bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-3.10.4.md)
- [plot](bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: flaskblogging, mypy, pylint
- new benchmarks: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
- [table](bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-3.11.0.md)
- [plot](bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-base.md)
- [plot](bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-1134727-vs-base.png)

