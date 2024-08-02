# Results

- fork: python
- version: 3.13.0a4+
- config: NOGIL
- commit hash: [2e94a66](https://github.com/python/cpython/commit/2e94a66)
- commit date: 2024-03-01T01:02:12+00:00
- commit merge base: [d7ddd90308324340855ddb9cc8dda2c1ee3a5944](https://github.com/python/cpython/commit/d7ddd90308324340855ddb9cc8dda2c1ee3a5944)
- ref: 2e94a6687c1a9750e9d2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9064106501)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240301-linux-x86_64-python-2e94a6687c1a9750e9d2-3.13.0a4%2B-2e94a66.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240301-linux-x86_64-python-2e94a6687c1a9750e9d2-3.13.0a4%2B-2e94a66-vs-3.10.4.md)
- [📈time plot](bm-20240301-linux-x86_64-python-2e94a6687c1a9750e9d2-3.13.0a4%2B-2e94a66-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 99.94%, 1.01x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240301-linux-x86_64-python-2e94a6687c1a9750e9d2-3.13.0a4%2B-2e94a66-vs-3.12.0.md)
- [📈time plot](bm-20240301-linux-x86_64-python-2e94a6687c1a9750e9d2-3.13.0a4%2B-2e94a66-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.10x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bpe_tokeniser, dask, djangocms
- [📄table](bm-20240301-linux-x86_64-python-2e94a6687c1a9750e9d2-3.13.0a4%2B-2e94a66-vs-3.13.0b2.md)
- [📈time plot](bm-20240301-linux-x86_64-python-2e94a6687c1a9750e9d2-3.13.0a4%2B-2e94a66-vs-3.13.0b2.svg)

