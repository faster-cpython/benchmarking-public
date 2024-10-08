# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: 
- commit hash: [a6f1035](https://github.com/brandtbucher/cpython/commit/a6f1035)
- commit date: 2024-09-21T23:12:25-07:00
- commit merge base: [6e06e01881dcffbeef5baac0c112ffb14cfa0b27](https://github.com/brandtbucher/cpython/commit/6e06e01881dcffbeef5baac0c112ffb14cfa0b27)
- ref: nojit

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 97.08%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 97.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 53.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240921-azure-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-pystats.json)
- [pystats table](bm-20240921-azure-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-pystats.md)

### vs. base

- [pystats diff](bm-20240921-azure-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 80.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 72.36%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 93.16%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 97.84%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.11x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 95.92%, 1.00x slower at 99th %ile)
- Memory usage: 0.48x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

