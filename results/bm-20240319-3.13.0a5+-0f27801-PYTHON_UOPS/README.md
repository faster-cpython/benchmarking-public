# Results

- fork: python
- version: 3.13.0a5+
- tier 2: True
- jit: False
- commit hash: [0f27801](https://github.com/python/cpython/commit/0f27801)
- commit date: 2024-03-19T11:06:43+00:00
- commit merge base: [5405e9e5b51f3bd883aee5c1a52a39a56e2fb2b4](https://github.com/python/cpython/commit/5405e9e5b51f3bd883aee5c1a52a39a56e2fb2b4)
- ref: 0f278012e88fa9607d85

## linux x86_64 (azure)

- [pystats raw](bm-20240319-azure-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-pystats.json)
- [pystats table](bm-20240319-azure-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8342515240)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.35
- [raw results](bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.10.4.md)
- [📈time plot](bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x slower (HPT: reliability of 98.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.11.0.md)
- [📈time plot](bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.12.0.md)
- [📈time plot](bm-20240319-pythonperf2-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.12.0.png)

