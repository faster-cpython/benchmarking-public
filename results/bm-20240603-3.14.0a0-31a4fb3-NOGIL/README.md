# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [31a4fb3](https://github.com/python/cpython/commit/31a4fb3)
- commit date: 2024-06-03T18:10:15-07:00
- commit merge base: [105f22ea46ac16866e6df18ebae2a8ba422b7f45](https://github.com/python/cpython/commit/105f22ea46ac16866e6df18ebae2a8ba422b7f45)
- ref: 31a4fb3c74a028443634

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9380328408)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3.json)

### vs. 3.10.4

- Geometric mean: 1.10x slower (HPT: reliability of 99.87%, 1.01x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.10.4.md)
- [📈time plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.37x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.12.0.md)
- [📈time plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.13.0b2.md)
- [📈time plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.46x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-base-mem.svg)
- [📄table](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-base.md)
- [📈time plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-base.svg)

