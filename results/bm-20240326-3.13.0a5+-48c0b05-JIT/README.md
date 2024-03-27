# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [48c0b05](https://github.com/python/cpython/commit/48c0b05)
- commit date: 2024-03-26T13:08:08-06:00
- commit merge base: [af1b0e94400d1bf732466d675054df8cf7dfb62d](https://github.com/python/cpython/commit/af1b0e94400d1bf732466d675054df8cf7dfb62d)
- ref: 48c0b05cf0dd2db275bd

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8447334369)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.10.4.md)
- [📈time plot](bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 60.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.11.0.md)
- [📈time plot](bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 73.16%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.12.0.md)
- [📈time plot](bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5%2B-48c0b05-vs-3.12.0.png)

