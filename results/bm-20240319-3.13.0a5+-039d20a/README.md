# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [039d20a](https://github.com/python/cpython/commit/039d20a)
- commit date: 2024-03-19T10:44:13+00:00
- commit merge base: [b1bc37597f0d36084c4dcb15977fe6d4b9322cd4](https://github.com/python/cpython/commit/b1bc37597f0d36084c4dcb15977fe6d4b9322cd4)
- ref: 039d20ae5428dfe3d704

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8376604583)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5%2B-039d20a.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5%2B-039d20a-vs-3.10.4.md)
- [📈time plot](bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5%2B-039d20a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.62%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5%2B-039d20a-vs-3.11.0.md)
- [📈time plot](bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5%2B-039d20a-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 98.04%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5%2B-039d20a-vs-3.12.0.md)
- [📈time plot](bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5%2B-039d20a-vs-3.12.0.png)

