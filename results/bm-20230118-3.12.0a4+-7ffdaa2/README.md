# Results

- fork: brandtbucher
- ref: quicken_in_compiler
- version: 3.12.0a4+
- commit hash: [7ffdaa2](https://github.com/brandtbucher/cpython/commit/7ffdaa2)
- commit date: 2023-01-18T02:27:14-08:00
- commit merge base: [ea232716d3de1675478db3a302629ba43194c967](https://github.com/brandtbucher/cpython/commit/ea232716d3de1675478db3a302629ba43194c967)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-pystats.json)
- [pystats table](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-pystats.md)
- [raw results](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2.json)

### vs. 3.10.4

- 1.31x faster \*
- missing benchmarks: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-vs-3.10.4.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
- [table](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-vs-3.11.0.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-vs-base.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-7ffdaa2-vs-base.png)

