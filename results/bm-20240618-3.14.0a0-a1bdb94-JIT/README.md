# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [a1bdb94](https://github.com/brandtbucher/cpython/commit/a1bdb94)
- commit date: 2024-06-18T15:35:06-07:00
- commit merge base: [9f741e55c16376412c1473aa45b94314c00a0c43](https://github.com/brandtbucher/cpython/commit/9f741e55c16376412c1473aa45b94314c00a0c43)
- ref: no_cold_exits

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9574547731)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.md)
- [📈time plot](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.md)
- [📈time plot](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 70.96%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base-mem.svg)
- [📄table](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.md)
- [📈time plot](bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240618-azure-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-pystats.json)
- [pystats table](bm-20240618-azure-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-pystats.md)

### vs. base

- [pystats diff](bm-20240618-azure-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9574547731)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.md)
- [📈time plot](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 97.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.md)
- [📈time plot](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 51.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 52.91%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base-mem.svg)
- [📄table](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.md)
- [📈time plot](bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9574547731)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.md)
- [📈time plot](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 70.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.md)
- [📈time plot](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 95.01%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 97.74%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base-mem.svg)
- [📄table](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.md)
- [📈time plot](bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9574547731)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.md)
- [📈time plot](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.md)
- [📈time plot](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 92.79%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize
- [📄table](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 89.85%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.md)
- [📈time plot](bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9574547731)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.md)
- [📈time plot](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.md)
- [📈time plot](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 98.01%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.60%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.md)
- [📈time plot](bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9574547731)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.md)
- [📈time plot](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.md)
- [📈time plot](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 63.45%, 1.00x slower at 99th %ile)
- Memory usage: 0.90x
- [🧠memory plot](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base-mem.svg)
- [📄table](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.md)
- [📈time plot](bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94-vs-base.svg)

