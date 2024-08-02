# Results

- fork: python
- version: 3.13.0b1+
- config: 
- commit hash: [6725c78](https://github.com/python/cpython/commit/6725c78)
- commit date: 2024-06-04T15:39:49+00:00
- ref: 6725c78d376eadb01a9d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 85.98%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 97.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240604-azure-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-pystats.json)
- [pystats table](bm-20240604-azure-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-linux-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 78.97%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 98.47%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 95.12%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 95.03%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9371154985)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 0.78x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.md)
- [📈time plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.77x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.md)
- [📈time plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 58.09%, 1.00x slower at 99th %ile)
- Memory usage: 0.52x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1%2B-6725c78-vs-3.13.0b2.svg)

