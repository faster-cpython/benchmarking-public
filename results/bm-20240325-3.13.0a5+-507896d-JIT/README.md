# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [507896d](https://github.com/python/cpython/commit/507896d)
- commit date: 2024-03-25T16:32:20+00:00
- commit merge base: [0c1a42cf9c8cd0d4534d5c1d58f118ce7c5c446e](https://github.com/python/cpython/commit/0c1a42cf9c8cd0d4534d5c1d58f118ce7c5c446e)
- ref: 507896d97dcff2d7999e

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8424439181)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.10.4.md)
- [📈time plot](bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 79.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.11.0.md)
- [📈time plot](bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 74.23%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.12.0.md)
- [📈time plot](bm-20240325-linux-x86_64-python-507896d97dcff2d7999e-3.13.0a5%2B-507896d-vs-3.12.0.png)

