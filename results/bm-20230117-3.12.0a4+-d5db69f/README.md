# Results

- fork: brandtbucher
- ref: load_attr_managed_di
- version: 3.12.0a4+
- commit hash: [d5db69f](https://github.com/brandtbucher/cpython/commit/d5db69f)
- commit date: 2023-01-17T01:46:44-08:00
- commit merge base: [1a9d8c750be83e6abb65769d312361fe9742de02](https://github.com/brandtbucher/cpython/commit/1a9d8c750be83e6abb65769d312361fe9742de02)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-pystats.json)
- [pystats table](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-pystats.md)
- [raw results](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-vs-3.10.4.md)
- [plot](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-vs-3.11.0.md)
- [plot](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-vs-base.md)
- [plot](bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4%2B-d5db69f-vs-base.png)

