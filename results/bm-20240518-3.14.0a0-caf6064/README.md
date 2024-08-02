# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [caf6064](https://github.com/python/cpython/commit/caf6064)
- commit date: 2024-05-18T22:40:51+00:00
- commit merge base: [30b4e9f9c42493136c58c56fee5553128bb32428](https://github.com/python/cpython/commit/30b4e9f9c42493136c58c56fee5553128bb32428)
- ref: caf6064a1bc15ac344af

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9143481233)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.md)
- [📈time plot](bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x slower (HPT: reliability of 83.03%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.md)
- [📈time plot](bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 53.46%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, gunicorn, mypy2
- [📄table](bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.md)
- [📈time plot](bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240518-azure-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-pystats.json)
- [pystats table](bm-20240518-azure-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9143481233)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.md)
- [📈time plot](bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.md)
- [📈time plot](bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.md)
- [📈time plot](bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9143481233)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.md)
- [📈time plot](bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x slower (HPT: reliability of 69.50%, 1.00x slower at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.md)
- [📈time plot](bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 90.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, gunicorn, mypy2
- [📄table](bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.md)
- [📈time plot](bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9143481233)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.md)
- [📈time plot](bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.md)
- [📈time plot](bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 97.39%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dulwich_log, mypy2
- [📄table](bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.md)
- [📈time plot](bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9143481233)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.md)
- [📈time plot](bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.md)
- [📈time plot](bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 74.08%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.md)
- [📈time plot](bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9143481233)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.62x
- missing benchmarks: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.md)
- [📈time plot](bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.54x
- missing benchmarks: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.md)
- [📈time plot](bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 97.71%, 1.00x faster at 99th %ile)
- Memory usage: 0.33x
- missing benchmarks: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2
- [📄table](bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.md)
- [📈time plot](bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064-vs-3.13.0b2.svg)

