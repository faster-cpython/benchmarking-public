# Results

- fork: python
- version: 3.13.0a4
- config: NOGIL
- commit hash: [9d34f60](https://github.com/python/cpython/commit/9d34f60)
- commit date: 2024-02-15T14:38:42+01:00
- commit merge base: [b0e5c35ded6d4a16d7a021c10c99bac94250edd0](https://github.com/python/cpython/commit/b0e5c35ded6d4a16d7a021c10c99bac94250edd0)
- ref: v3.13.0a4

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038492160)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 98.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.12x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bpe_tokeniser, dask, djangocms
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.12x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base-mem.svg)
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.svg)

