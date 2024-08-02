# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [9f741e5](https://github.com/python/cpython/commit/9f741e5)
- commit date: 2024-06-18T22:13:45+00:00
- commit merge base: [b7f478948fcf3bf8e62c79ebcb3ff69bf06d9c4d](https://github.com/python/cpython/commit/b7f478948fcf3bf8e62c79ebcb3ff69bf06d9c4d)
- ref: 9f741e55c16376412c14

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.md)
- [📈time plot](bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.md)
- [📈time plot](bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240618-azure-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-pystats.json)
- [pystats table](bm-20240618-azure-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.md)
- [📈time plot](bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 97.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.md)
- [📈time plot](bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 50.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.md)
- [📈time plot](bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 72.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.md)
- [📈time plot](bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 96.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.md)
- [📈time plot](bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.md)
- [📈time plot](bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 96.64%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize
- [📄table](bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.md)
- [📈time plot](bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.md)
- [📈time plot](bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 95.95%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.md)
- [📈time plot](bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.md)
- [📈time plot](bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5-vs-3.13.0b2.svg)

