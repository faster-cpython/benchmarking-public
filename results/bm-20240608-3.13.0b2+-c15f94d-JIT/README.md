# Results

- fork: python
- version: 3.13.0b2+
- config: JIT
- commit hash: [c15f94d](https://github.com/python/cpython/commit/c15f94d)
- commit date: 2024-06-08T17:48:47+00:00
- ref: c15f94d6fbc960790db3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9432386312)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.md)
- [📈time plot](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.md)
- [📈time plot](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.md)
- [📈time plot](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base-mem.svg)
- [📄table](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.md)
- [📈time plot](bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9432386312)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 90.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 93.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 80.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base-mem.svg)
- [📄table](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.md)
- [📈time plot](bm-20240608-linux-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9432386312)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.md)
- [📈time plot](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 69.05%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.md)
- [📈time plot](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 95.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.md)
- [📈time plot](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 97.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base-mem.svg)
- [📄table](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.md)
- [📈time plot](bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9432386312)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.md)
- [📈time plot](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.33%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.md)
- [📈time plot](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlglot_normalize
- [📄table](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.md)
- [📈time plot](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 sqlglot_normalize
- [📄table](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.md)
- [📈time plot](bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9432386312)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.md)
- [📈time plot](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.md)
- [📈time plot](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 83.74%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.md)
- [📈time plot](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 88.76%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.md)
- [📈time plot](bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9432386312)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 0.71x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.md)
- [📈time plot](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.md)
- [📈time plot](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.78%, 1.00x slower at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: bpe_tokeniser, sqlglot_normalize
- [📄table](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.md)
- [📈time plot](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: 🔴 sqlglot_normalize
- [🧠memory plot](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base-mem.svg)
- [📄table](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.md)
- [📈time plot](bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2%2B-c15f94d-vs-base.svg)

