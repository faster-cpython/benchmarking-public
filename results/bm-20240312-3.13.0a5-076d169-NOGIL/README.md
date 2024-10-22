# Results

- fork: python
- version: 3.13.0a5
- config: NOGIL
- commit hash: [076d169](https://github.com/python/cpython/commit/076d169)
- commit date: 2024-03-12T21:11:08+01:00
- commit merge base: [f6e7a6ce651b43c6e060608a4bb20685f39e9eaa](https://github.com/python/cpython/commit/f6e7a6ce651b43c6e060608a4bb20685f39e9eaa)
- ref: v3.13.0a5

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038496952)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.09x slower (HPT: reliability of 99.97%, 1.01x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.35x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bpe_tokeniser, dask, djangocms, unpack_sequence
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.43x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: 🔴 dask, djangocms
- [🧠memory plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-base-mem.svg)
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-base.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.svg)

