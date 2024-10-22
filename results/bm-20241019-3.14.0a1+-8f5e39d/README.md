# Results

- fork: python
- version: 3.14.0a1+
- config: 
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

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 92.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log, sphinx
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241019-azure-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-pystats.json)
- [pystats table](bm-20241019-azure-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 71.29%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 97.53%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x slower (HPT: reliability of 99.82%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.11x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 99.71%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: sphinx
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 6.09x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

