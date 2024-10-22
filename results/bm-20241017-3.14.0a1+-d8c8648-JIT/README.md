# Results

- fork: python
- version: 3.14.0a1+
- config: JIT
- commit hash: [d8c8648](https://github.com/python/cpython/commit/d8c8648)
- commit date: 2024-10-17T20:10:55+02:00
- commit merge base: [b454662921fd3a1fc27169e91aca03aadea08817](https://github.com/python/cpython/commit/b454662921fd3a1fc27169e91aca03aadea08817)
- ref: d8c864816121547338ef

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.18x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log, sphinx
- [📄table](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241017-azure-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-pystats.json)
- [pystats table](bm-20241017-azure-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 82.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 74.70%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x slower (HPT: reliability of 81.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 73.14%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x slower (HPT: reliability of 99.90%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.06x faster (HPT: reliability of 82.30%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: sphinx
- [📄table](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 97.56%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.34%, 1.00x faster at 99th %ile)
- Memory usage: 6.45x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx
- [📄table](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.md)
- [📈time plot](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0b2.svg)

