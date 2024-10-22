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

- Geometric mean: 1.09x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: 1.37x
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

### vs. 3.13.0

- Geometric mean: 1.18x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log, sphinx
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-arminc-aarch64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

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

- Geometric mean: 1.04x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 67.06%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 56.53%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-linux-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 80.07%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x slower (HPT: reliability of 74.54%, 1.00x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf2-x86_64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

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

- Geometric mean: 1.00x faster (HPT: reliability of 80.39%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x slower (HPT: reliability of 99.89%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.02x faster (HPT: reliability of 81.93%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf1-amd64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.05x faster (HPT: reliability of 66.72%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: sphinx
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.04x faster (HPT: reliability of 68.81%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-pythonperf1_win32-x86-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11421710436)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.80%, 1.00x faster at 99th %ile)
- Memory usage: 6.63x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.05x slower (HPT: reliability of 99.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base-mem.svg)
- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.md)
- [📈time plot](bm-20241019-darwin-arm64-python-8f5e39d5c885318e3128-3.14.0a1%2B-8f5e39d-vs-3.13.0b2.svg)

