# Results

- fork: python
- version: 3.13.0b1+
- config: T2
- commit hash: [6725c78](https://github.com/python/cpython/commit/6725c78)
- commit date: 2024-06-04T15:39:49+00:00
- ref: 6725c78d376eadb01a9d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base-mem.svg)
- [📄table](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.md)
- [📈time plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240604-azure-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-pystats.json)
- [pystats table](bm-20240604-azure-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-pystats.md)

### vs. base

- [pystats diff](bm-20240604-azure-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.01x faster (HPT: reliability of 95.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.27x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.30x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.31x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base-mem.svg)
- [📄table](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.md)
- [📈time plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base-mem.svg)
- [📄table](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.md)
- [📈time plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.79%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlglot_normalize
- [📄table](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 sqlglot_normalize
- [📄table](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.md)
- [📈time plot](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.md)
- [📈time plot](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.11x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.74x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 99.93%, 1.01x slower at 99th %ile)
- Memory usage: 0.65x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: bpe_tokeniser, sqlglot_normalize
- [📄table](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: 🔴 sqlglot_normalize
- [🧠memory plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base-mem.svg)
- [📄table](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.md)
- [📈time plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-base.svg)

