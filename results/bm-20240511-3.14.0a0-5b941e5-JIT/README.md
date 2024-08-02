# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [5b941e5](https://github.com/python/cpython/commit/5b941e5)
- commit date: 2024-05-11T16:19:31-07:00
- commit merge base: [abead548af0172dabba13da8bacf2da3c02d4927](https://github.com/python/cpython/commit/abead548af0172dabba13da8bacf2da3c02d4927)
- ref: 5b941e57c71d7d0ab983

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9047257150)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.md)
- [📈time plot](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.md)
- [📈time plot](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, bpe_tokeniser, gunicorn, mypy2
- [📄table](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base-mem.svg)
- [📄table](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.md)
- [📈time plot](bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9047257150)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.md)
- [📈time plot](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 99.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.md)
- [📈time plot](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 61.23%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 83.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base-mem.svg)
- [📄table](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.md)
- [📈time plot](bm-20240511-linux-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9047257150)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.md)
- [📈time plot](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 55.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.md)
- [📈time plot](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 98.15%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, gunicorn, mypy2
- [📄table](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 91.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base-mem.svg)
- [📄table](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.md)
- [📈time plot](bm-20240511-pythonperf2-x86_64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9047257150)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.md)
- [📈time plot](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.34%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.md)
- [📈time plot](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 99.89%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dulwich_log, mypy2, sqlglot_normalize
- [📄table](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.28%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 sqlglot_normalize
- [📄table](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.md)
- [📈time plot](bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9047257150)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.md)
- [📈time plot](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.md)
- [📈time plot](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 93.07%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 92.03%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.md)
- [📈time plot](bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9047257150)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.md)
- [📈time plot](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.79x
- missing benchmarks: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.md)
- [📈time plot](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.74x
- missing benchmarks: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2, sqlglot_normalize
- [📄table](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.md)
- [📈time plot](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: 🔴 sqlglot_normalize
- [🧠memory plot](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base-mem.svg)
- [📄table](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.md)
- [📈time plot](bm-20240511-darwin-arm64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5-vs-base.svg)

