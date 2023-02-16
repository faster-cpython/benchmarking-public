# Results

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- version: 3.12.0a4+
- commit hash: [23ae36b](https://github.com/iritkatriel/cpython/commit/23ae36b)
- commit date: 2023-01-29T21:19:07+00:00
- commit merge base: [409f5337a3e466a5ef673797575cbd1745d27ca9](https://github.com/iritkatriel/cpython/commit/409f5337a3e466a5ef673797575cbd1745d27ca9)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4%2B-23ae36b.json)

### vs. 3.10.4

- 1.31x faster \*
- missing benchmarks: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4%2B-23ae36b-vs-3.10.4.md)
- [plot](bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4%2B-23ae36b-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4%2B-23ae36b-vs-3.11.0.md)
- [plot](bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4%2B-23ae36b-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4%2B-23ae36b-vs-base.md)
- [plot](bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4%2B-23ae36b-vs-base.png)

