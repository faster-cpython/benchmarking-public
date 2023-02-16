# Results

- fork: brandtbucher
- ref: compare_and_not_bran
- version: 3.12.0a4+
- commit hash: [53e50c4](https://github.com/brandtbucher/cpython/commit/53e50c4)
- commit date: 2023-02-01T12:58:36-08:00
- commit merge base: [7840ff3cdbdf64f517c9f981f57eff232e676104](https://github.com/brandtbucher/cpython/commit/7840ff3cdbdf64f517c9f981f57eff232e676104)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-pystats.json)
- [pystats table](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-pystats.md)
- [raw results](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-vs-3.10.4.md)
- [plot](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-vs-3.11.0.md)
- [plot](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-vs-base.md)
- [plot](bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4%2B-53e50c4-vs-base.png)

