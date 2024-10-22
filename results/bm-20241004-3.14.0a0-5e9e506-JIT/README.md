# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [5e9e506](https://github.com/python/cpython/commit/5e9e506)
- commit date: 2024-10-04T02:00:32+02:00
- commit merge base: [c8db0e817e7e0db501533fc8bf5b30c18e60aa3d](https://github.com/python/cpython/commit/c8db0e817e7e0db501533fc8bf5b30c18e60aa3d)
- ref: 5e9e50612eb27aef8f74

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.md)
- [📈time plot](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.md)
- [📈time plot](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log, sphinx
- [📄table](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.md)
- [📈time plot](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241004-azure-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-pystats.json)
- [pystats table](bm-20241004-azure-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.md)
- [📈time plot](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.md)
- [📈time plot](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 53.55%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.md)
- [📈time plot](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 91.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- new benchmarks: sphinx
- [🧠memory plot](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-base-mem.svg)
- [📄table](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-base.md)
- [📈time plot](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.md)
- [📈time plot](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 77.02%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.md)
- [📈time plot](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x slower (HPT: reliability of 56.38%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.md)
- [📈time plot](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.md)
- [📈time plot](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 55.75%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.md)
- [📈time plot](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x slower (HPT: reliability of 99.94%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.md)
- [📈time plot](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.md)
- [📈time plot](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.md)
- [📈time plot](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x faster (HPT: reliability of 92.24%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: sphinx
- [📄table](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.md)
- [📈time plot](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394701974)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.md)
- [📈time plot](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 98.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.md)
- [📈time plot](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.80%, 1.00x faster at 99th %ile)
- Memory usage: 6.58x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.md)
- [📈time plot](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.md)
- [📈time plot](bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506-vs-3.13.0b2.svg)

