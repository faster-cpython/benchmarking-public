# Results

- fork: python
- version: 3.14.0a1+
- config: JIT
- commit hash: [8f5e39d](https://github.com/python/cpython/commit/8f5e39d)
- commit date: 2024-10-19T17:46:57-04:00
- commit merge base: [4c53b2577531c77193430cdcd66ad6385fcda81f](https://github.com/python/cpython/commit/4c53b2577531c77193430cdcd66ad6385fcda81f)
- ref: 8f5e39d5c885318e3128

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.07x
- [🧠memory plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 73.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 84.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 76.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 99.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 73.16%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 99.92%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x faster (HPT: reliability of 80.88%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.78%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, sphinx, unpack_sequence
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x faster (HPT: reliability of 65.61%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

