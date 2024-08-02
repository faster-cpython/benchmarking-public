# Results

- fork: python
- version: 3.13.0a4+
- config: NOGIL
- commit hash: [339c8e1](https://github.com/python/cpython/commit/339c8e1)
- commit date: 2024-02-29T21:53:32-05:00
- commit merge base: [2e94a6687c1a9750e9d2408a8dff0a422aeaf0e4](https://github.com/python/cpython/commit/2e94a6687c1a9750e9d2408a8dff0a422aeaf0e4)
- ref: 339c8e1c13adc299a0e2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9064106501)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1.json)

### vs. 3.10.4

- Geometric mean: 1.07x slower (HPT: reliability of 98.33%, 1.00x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-3.10.4.md)
- [📈time plot](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.32x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-3.12.0.md)
- [📈time plot](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bpe_tokeniser, dask, djangocms
- [📄table](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-3.13.0b2.md)
- [📈time plot](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.27x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-base-mem.svg)
- [📄table](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-base.md)
- [📈time plot](bm-20240229-linux-x86_64-python-339c8e1c13adc299a0e2-3.13.0a4%2B-339c8e1-vs-base.svg)

