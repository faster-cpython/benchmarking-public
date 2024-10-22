# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [5436d8b](https://github.com/python/cpython/commit/5436d8b)
- commit date: 2024-09-11T07:49:59-07:00
- commit merge base: [6e23c89fcdd02b08fa6e9fa70d6e90763ddfc327](https://github.com/python/cpython/commit/6e23c89fcdd02b08fa6e9fa70d6e90763ddfc327)
- ref: 5436d8b9c397c48d9b0d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.md)
- [📈time plot](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.70%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.md)
- [📈time plot](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log
- [📄table](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.md)
- [📈time plot](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.md)
- [📈time plot](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.md)
- [📈time plot](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.md)
- [📈time plot](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 84.10%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 81.49%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- [📄table](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json)

### vs. 3.10.4

- Geometric mean: 1.11x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 98.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.83x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.md)
- [📈time plot](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.75x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.md)
- [📈time plot](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.md)
- [📈time plot](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-darwin-arm64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b-vs-3.13.0b2.svg)

