# Results

- fork: python
- version: 3.13.0a5
- config: 
- commit hash: [076d169](https://github.com/python/cpython/commit/076d169)
- commit date: 2024-03-12T21:11:08+01:00
- commit merge base: [f6e7a6ce651b43c6e060608a4bb20685f39e9eaa](https://github.com/python/cpython/commit/f6e7a6ce651b43c6e060608a4bb20685f39e9eaa)
- ref: v3.13.0a5

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 89.83%, 1.00x faster at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 64.97%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.md)
- [📈time plot](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 98.67%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 98.40%, 1.00x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 74.83%, 1.00x slower at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.md)
- [📈time plot](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.md)
- [📈time plot](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.09%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.md)
- [📈time plot](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 0.48x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 98.55%, 1.00x slower at 99th %ile)
- Memory usage: 0.49x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.43x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.md)
- [📈time plot](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0b2.svg)

