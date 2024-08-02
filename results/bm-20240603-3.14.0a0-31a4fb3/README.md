# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [31a4fb3](https://github.com/python/cpython/commit/31a4fb3)
- commit date: 2024-06-03T18:10:15-07:00
- commit merge base: [105f22ea46ac16866e6df18ebae2a8ba422b7f45](https://github.com/python/cpython/commit/105f22ea46ac16866e6df18ebae2a8ba422b7f45)
- ref: 31a4fb3c74a028443634

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9364039451)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.10.4.md)
- [📈time plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.12.0.md)
- [📈time plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.13.0b2.md)
- [📈time plot](bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9364106694)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.10.4.md)
- [📈time plot](bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 57.53%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.12.0.md)
- [📈time plot](bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 98.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.13.0b2.md)
- [📈time plot](bm-20240603-pythonperf2-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3-vs-3.13.0b2.svg)

