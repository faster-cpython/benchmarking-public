# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [c8db0e8](https://github.com/python/cpython/commit/c8db0e8)
- commit date: 2024-10-03T21:06:29+01:00
- commit merge base: [7ecaf21946a1da0ede664447839537a7fc5eb64e](https://github.com/python/cpython/commit/7ecaf21946a1da0ede664447839537a7fc5eb64e)
- ref: c8db0e817e7e0db50153

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.md)
- [📈time plot](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 94.84%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.md)
- [📈time plot](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.06x slower (HPT: reliability of 91.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log
- [📄table](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.md)
- [📈time plot](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.md)
- [📈time plot](bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241003-azure-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-pystats.json)
- [pystats table](bm-20241003-azure-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json)

### vs. 3.10.4

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.md)
- [📈time plot](bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.md)
- [📈time plot](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 81.57%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.md)
- [📈time plot](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.md)
- [📈time plot](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.md)
- [📈time plot](bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.md)
- [📈time plot](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x slower (HPT: reliability of 99.96%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.md)
- [📈time plot](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- [📄table](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.md)
- [📈time plot](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.md)
- [📈time plot](bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.md)
- [📈time plot](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.11x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.md)
- [📈time plot](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.md)
- [📈time plot](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.md)
- [📈time plot](bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8-vs-3.13.0b2.svg)

