# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [ec9d12b](https://github.com/python/cpython/commit/ec9d12b)
- commit date: 2024-05-10T16:55:49+00:00
- commit merge base: [f5c6b9977a561fcf9c2a803fb08652fd39b13d3b](https://github.com/python/cpython/commit/f5c6b9977a561fcf9c2a803fb08652fd39b13d3b)
- ref: main

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9036769991)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b.json)

### vs. 3.10.4

- Geometric mean: 1.17x slower (HPT: reliability of 99.98%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, dask, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-3.10.4.md)
- [📈time plot](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-3.12.0.md)
- [📈time plot](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.53x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, bpe_tokeniser, dask, djangocms, gunicorn, mypy2
- [📄table](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-3.13.0b2.md)
- [📈time plot](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.49x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-base-mem.svg)
- [📄table](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-base.md)
- [📈time plot](bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b-vs-base.svg)

