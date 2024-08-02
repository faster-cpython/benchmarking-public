# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [f837cc6](https://github.com/brandtbucher/cpython/commit/f837cc6)
- commit date: 2024-06-10T12:46:48-07:00
- commit merge base: [e83ce850f433fd8bbf8ff4e8d7649b942639db31](https://github.com/brandtbucher/cpython/commit/e83ce850f433fd8bbf8ff4e8d7649b942639db31)
- ref: no_cold_exits

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.md)
- [📈time plot](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.md)
- [📈time plot](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.md)
- [📈time plot](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 94.96%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base-mem.svg)
- [📄table](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.md)
- [📈time plot](bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240610-azure-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-pystats.json)
- [pystats table](bm-20240610-azure-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-pystats.md)

### vs. base

- [pystats diff](bm-20240610-azure-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.md)
- [📈time plot](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.md)
- [📈time plot](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 56.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.md)
- [📈time plot](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.74%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base-mem.svg)
- [📄table](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.md)
- [📈time plot](bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.md)
- [📈time plot](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 64.51%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.md)
- [📈time plot](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 95.74%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.md)
- [📈time plot](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base-mem.svg)
- [📄table](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.md)
- [📈time plot](bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.md)
- [📈time plot](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.92%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.md)
- [📈time plot](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 99.94%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize
- [📄table](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.md)
- [📈time plot](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 90.33%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.md)
- [📈time plot](bm-20240610-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.md)
- [📈time plot](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.md)
- [📈time plot](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x faster (HPT: reliability of 62.11%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.md)
- [📈time plot](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 96.96%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.md)
- [📈time plot](bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9454599291)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.md)
- [📈time plot](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.85x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.md)
- [📈time plot](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlglot_normalize
- [📄table](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.md)
- [📈time plot](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 95.49%, 1.00x faster at 99th %ile)
- Memory usage: 0.86x
- [🧠memory plot](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base-mem.svg)
- [📄table](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.md)
- [📈time plot](bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6-vs-base.svg)

