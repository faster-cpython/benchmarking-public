# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [e83ce85](https://github.com/python/cpython/commit/e83ce85)
- commit date: 2024-06-05T18:54:50+01:00
- commit merge base: [14e3c7071bd1add30d4b69b62e011c7d38aebd9b](https://github.com/python/cpython/commit/14e3c7071bd1add30d4b69b62e011c7d38aebd9b)
- ref: e83ce850f433fd8bbf8f

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.md)
- [📈time plot](bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.md)
- [📈time plot](bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.md)
- [📈time plot](bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240605-azure-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-pystats.json)
- [pystats table](bm-20240605-azure-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.md)
- [📈time plot](bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 97.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.md)
- [📈time plot](bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 73.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.md)
- [📈time plot](bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.md)
- [📈time plot](bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 51.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.md)
- [📈time plot](bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 97.56%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.md)
- [📈time plot](bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.md)
- [📈time plot](bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.23%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.md)
- [📈time plot](bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 99.82%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize
- [📄table](bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.md)
- [📈time plot](bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.md)
- [📈time plot](bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.md)
- [📈time plot](bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 66.96%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.md)
- [📈time plot](bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.md)
- [📈time plot](bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.62x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.md)
- [📈time plot](bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlglot_normalize
- [📄table](bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.md)
- [📈time plot](bm-20240605-darwin-arm64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85-vs-3.13.0b2.svg)

