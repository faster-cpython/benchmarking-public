# Results

- fork: python
- version: 3.13.0
- config: 
- commit hash: [60403a5](https://github.com/python/cpython/commit/60403a5)
- commit date: 2024-10-07T07:02:14+02:00
- ref: v3.13.0

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11257188871)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 97.91%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11257188871)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11257188871)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 63.18%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11257188871)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11257188871)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11257188871)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 0.54x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.md)
- [📈time plot](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 90.11%, 1.00x slower at 99th %ile)
- Memory usage: 0.49x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.md)
- [📈time plot](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.12.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5-vs-3.13.0b2.svg)

