# Results

- fork: brandtbucher
- ref: remove_old_branch
- version: 3.12.0a4+
- commit hash: [b1845b6](https://github.com/brandtbucher/cpython/commit/b1845b6)
- commit date: 2023-01-18T03:01:42-08:00
- commit merge base: [1a9d8c750be83e6abb65769d312361fe9742de02](https://github.com/brandtbucher/cpython/commit/1a9d8c750be83e6abb65769d312361fe9742de02)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.10.4.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.11.0.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-base.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-remove_old_branch-3.12.0a4%2B-b1845b6-vs-base.png)

