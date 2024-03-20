# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [0f27801](https://github.com/python/cpython/commit/0f27801)
- commit date: 2024-03-19T11:06:43+00:00
- commit merge base: [5405e9e5b51f3bd883aee5c1a52a39a56e2fb2b4](https://github.com/python/cpython/commit/5405e9e5b51f3bd883aee5c1a52a39a56e2fb2b4)
- ref: 0f278012e88fa9607d85

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8361751801)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.10.4.md)
- [📈time plot](bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 70.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.11.0.md)
- [📈time plot](bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 71.69%, 1.00x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.12.0.md)
- [📈time plot](bm-20240319-linux-x86_64-python-0f278012e88fa9607d85-3.13.0a5%2B-0f27801-vs-3.12.0.png)

