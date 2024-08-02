# Results

- fork: python
- version: 3.13.0b1+
- config: 
- commit hash: [44995aa](https://github.com/python/cpython/commit/44995aa)
- commit date: 2024-05-13T11:56:26+00:00
- commit merge base: [2268289a47c6e3c9a220b53697f9480ec390466f](https://github.com/python/cpython/commit/2268289a47c6e3c9a220b53697f9480ec390466f)
- ref: 44995aab499b09a550de

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9063825220)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.md)
- [📈time plot](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x slower (HPT: reliability of 71.71%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.md)
- [📈time plot](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 88.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.md)
- [📈time plot](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base-mem.svg)
- [📄table](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.md)
- [📈time plot](bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9063825220)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.md)
- [📈time plot](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 99.61%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.md)
- [📈time plot](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 98.37%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.md)
- [📈time plot](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base-mem.svg)
- [📄table](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.md)
- [📈time plot](bm-20240513-linux-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9063825220)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.md)
- [📈time plot](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 79.29%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.md)
- [📈time plot](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 99.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.md)
- [📈time plot](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base-mem.svg)
- [📄table](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.md)
- [📈time plot](bm-20240513-pythonperf2-x86_64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9063825220)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.md)
- [📈time plot](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.md)
- [📈time plot](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 98.12%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.md)
- [📈time plot](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 dask
- [📄table](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.md)
- [📈time plot](bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9063825220)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1%2B-44995aa.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.md)
- [📈time plot](bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.md)
- [📈time plot](bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 88.90%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.md)
- [📈time plot](bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9063825220)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.68x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.md)
- [📈time plot](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.60x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.md)
- [📈time plot](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 94.92%, 1.00x faster at 99th %ile)
- Memory usage: 0.43x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.md)
- [📈time plot](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.34x
- [🧠memory plot](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base-mem.svg)
- [📄table](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.md)
- [📈time plot](bm-20240513-darwin-arm64-python-44995aab499b09a550de-3.13.0b1%2B-44995aa-vs-base.svg)

