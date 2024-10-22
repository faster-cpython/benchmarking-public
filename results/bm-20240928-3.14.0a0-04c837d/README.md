# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [04c837d](https://github.com/python/cpython/commit/04c837d)
- commit date: 2024-09-28T15:15:43-07:00
- commit merge base: [69a4063ca516360b5eb96f5432ad9f9dfc32a72e](https://github.com/python/cpython/commit/69a4063ca516360b5eb96f5432ad9f9dfc32a72e)
- ref: 04c837d9d8a474777ef9

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 98.65%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: dulwich_log
- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-arminc-aarch64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240928-azure-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-pystats.json)
- [pystats table](bm-20240928-azure-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 98.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-linux-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 86.07%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x slower (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-pythonperf2-x86_64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11087962556)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.58x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.md)
- [📈time plot](bm-20240928-darwin-arm64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d-vs-3.13.0b2.svg)

