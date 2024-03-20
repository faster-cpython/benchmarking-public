# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [025ef7a](https://github.com/python/cpython/commit/025ef7a)
- commit date: 2024-03-19T13:55:21-04:00
- commit merge base: [b85572c47dc7a8c65fc366a87a3660fc7a3ed244](https://github.com/python/cpython/commit/b85572c47dc7a8c65fc366a87a3660fc7a3ed244)
- ref: 025ef7a5f7b424fba871

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8351032410)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5%2B-025ef7a.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5%2B-025ef7a-vs-3.10.4.md)
- [📈time plot](bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5%2B-025ef7a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 73.65%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5%2B-025ef7a-vs-3.11.0.md)
- [📈time plot](bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5%2B-025ef7a-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 84.25%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5%2B-025ef7a-vs-3.12.0.md)
- [📈time plot](bm-20240319-linux-x86_64-python-025ef7a5f7b424fba871-3.13.0a5%2B-025ef7a-vs-3.12.0.png)

