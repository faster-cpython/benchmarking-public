# Results

- fork: python
- version: 3.13.0b2+
- config: 
- commit hash: [a19bb26](https://github.com/python/cpython/commit/a19bb26)
- commit date: 2024-06-15T19:10:50+00:00
- ref: a19bb261a327e1008f21

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9531723880)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240615-arminc-aarch64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240615-arminc-aarch64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.md)
- [📈time plot](bm-20240615-arminc-aarch64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 81.98%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging
- [📄table](bm-20240615-arminc-aarch64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.md)
- [📈time plot](bm-20240615-arminc-aarch64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 59.56%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20240615-arminc-aarch64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-arminc-aarch64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240615-azure-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-pystats.json)
- [pystats table](bm-20240615-azure-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9531723880)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240615-linux-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240615-linux-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.md)
- [📈time plot](bm-20240615-linux-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.30%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240615-linux-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.md)
- [📈time plot](bm-20240615-linux-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 65.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20240615-linux-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-linux-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9531723880)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240615-pythonperf2-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240615-pythonperf2-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.md)
- [📈time plot](bm-20240615-pythonperf2-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 89.52%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240615-pythonperf2-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.md)
- [📈time plot](bm-20240615-pythonperf2-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 98.31%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20240615-pythonperf2-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-pythonperf2-x86_64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9531723880)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.md)
- [📈time plot](bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.md)
- [📈time plot](bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.94%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9531723880)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240615-pythonperf1_win32-x86-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240615-pythonperf1_win32-x86-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.md)
- [📈time plot](bm-20240615-pythonperf1_win32-x86-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240615-pythonperf1_win32-x86-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.md)
- [📈time plot](bm-20240615-pythonperf1_win32-x86-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.36%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240615-pythonperf1_win32-x86-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-pythonperf1_win32-x86-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9531723880)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240615-darwin-arm64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240615-darwin-arm64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.md)
- [📈time plot](bm-20240615-darwin-arm64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240615-darwin-arm64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.md)
- [📈time plot](bm-20240615-darwin-arm64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 98.03%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [📄table](bm-20240615-darwin-arm64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-darwin-arm64-python-a19bb261a327e1008f21-3.13.0b2%2B-a19bb26-vs-3.13.0b2.svg)

