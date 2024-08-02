# Results

- fork: python
- version: 3.13.0a6+
- config: JIT
- commit hash: [b034f14](https://github.com/python/cpython/commit/b034f14)
- commit date: 2024-05-04T12:12:10+01:00
- commit merge base: [1ab6356ebec25f216a0eddbd81225abcb93f2d55](https://github.com/python/cpython/commit/1ab6356ebec25f216a0eddbd81225abcb93f2d55)
- ref: b034f14a4b6e9197d392

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8950111256)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6%2B-b034f14.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6%2B-b034f14-vs-3.10.4.md)
- [📈time plot](bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6%2B-b034f14-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 90.24%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6%2B-b034f14-vs-3.12.0.md)
- [📈time plot](bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6%2B-b034f14-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 95.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, docutils
- [📄table](bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6%2B-b034f14-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-linux-x86_64-python-b034f14a4b6e9197d392-3.13.0a6%2B-b034f14-vs-3.13.0b2.svg)

