# Results

- fork: python
- version: 3.13.0a3
- config: NOGIL
- commit hash: [f009305](https://github.com/python/cpython/commit/f009305)
- commit date: 2024-01-17T13:14:40+01:00
- commit merge base: [b204c4beb44c1a9013f8da16984c9129374ed8c5](https://github.com/python/cpython/commit/b204c4beb44c1a9013f8da16984c9129374ed8c5)
- ref: v3.13.0a3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9036778221)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, dask, djangocms
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base-mem.svg)
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

