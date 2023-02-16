# Results

- fork: carljm
- ref: inlinecomp2
- version: 3.12.0a5+
- commit hash: [ae0bd02](https://github.com/carljm/cpython/commit/ae0bd02)
- commit date: 2023-02-13T06:29:58-08:00
- commit merge base: [95cbb3d908175ccd855078b3fab7f99e7d0bca88](https://github.com/carljm/cpython/commit/95cbb3d908175ccd855078b3fab7f99e7d0bca88)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-ae0bd02.json)

### vs. 3.10.4

- 1.31x faster
- missing benchmarks: dask, flaskblogging, pylint
- [table](bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-ae0bd02-vs-3.10.4.md)
- [plot](bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-ae0bd02-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: flaskblogging, mypy, pylint
- new benchmarks: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
- [table](bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-ae0bd02-vs-3.11.0.md)
- [plot](bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-ae0bd02-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-ae0bd02-vs-base.md)
- [plot](bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-ae0bd02-vs-base.png)

