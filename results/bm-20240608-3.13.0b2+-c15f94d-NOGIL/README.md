# Results

- fork: python
- version: 3.13.0b2+
- config: NOGIL
- commit hash: [c15f94d](https://github.com/python/cpython/commit/c15f94d)
- commit date: 2024-06-08T17:48:47+00:00
- ref: c15f94d6fbc960790db3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9521445104)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d.json)

### vs. 3.10.4

- Geometric mean: 1.11x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.37x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: dask, djangocms
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: 🔴 dask, djangocms
- new benchmarks: bpe_tokeniser
- [🧠memory plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base-mem.svg)
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.svg)

