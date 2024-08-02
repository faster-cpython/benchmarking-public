# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [e04d5ab](https://github.com/brandtbucher/cpython/commit/e04d5ab)
- commit date: 2024-06-19T15:50:23-07:00
- commit merge base: [9f741e55c16376412c1473aa45b94314c00a0c43](https://github.com/brandtbucher/cpython/commit/9f741e55c16376412c1473aa45b94314c00a0c43)
- ref: justin_compact

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9589128588)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.md)
- [📈time plot](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.md)
- [📈time plot](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.md)
- [📈time plot](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base-mem.svg)
- [📄table](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.md)
- [📈time plot](bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240619-azure-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-pystats.json)
- [pystats table](bm-20240619-azure-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-pystats.md)

### vs. base

- [pystats diff](bm-20240619-azure-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9589128588)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.md)
- [📈time plot](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 96.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.md)
- [📈time plot](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 72.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.md)
- [📈time plot](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base-mem.svg)
- [📄table](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.md)
- [📈time plot](bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9589128588)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.md)
- [📈time plot](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 53.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.md)
- [📈time plot](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 94.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.md)
- [📈time plot](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.72%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base-mem.svg)
- [📄table](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.md)
- [📈time plot](bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9589128588)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.md)
- [📈time plot](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.md)
- [📈time plot](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 98.23%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize
- [📄table](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.md)
- [📈time plot](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 98.88%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.md)
- [📈time plot](bm-20240619-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9589128588)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.md)
- [📈time plot](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.md)
- [📈time plot](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 98.61%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.md)
- [📈time plot](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 70.61%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.md)
- [📈time plot](bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9589128588)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.md)
- [📈time plot](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 96.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.md)
- [📈time plot](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlglot_normalize
- [📄table](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.md)
- [📈time plot](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: 🔴 sqlglot_normalize
- [🧠memory plot](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base-mem.svg)
- [📄table](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.md)
- [📈time plot](bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab-vs-base.svg)

