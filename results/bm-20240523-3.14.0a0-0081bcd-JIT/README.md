# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [0081bcd](https://github.com/brandtbucher/cpython/commit/0081bcd)
- commit date: 2024-05-23T11:40:34-04:00
- commit merge base: [d472b4f9fa4fb6061588d421f33a0388a2005bc6](https://github.com/brandtbucher/cpython/commit/d472b4f9fa4fb6061588d421f33a0388a2005bc6)
- ref: justin_align

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9217931145)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.md)
- [📈time plot](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.md)
- [📈time plot](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, gunicorn, mypy2
- [📄table](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base-mem.svg)
- [📄table](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.md)
- [📈time plot](bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9217931145)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.md)
- [📈time plot](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 98.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.md)
- [📈time plot](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 75.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 52.33%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base-mem.svg)
- [📄table](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.md)
- [📈time plot](bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9217931145)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.md)
- [📈time plot](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 67.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.md)
- [📈time plot](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 95.30%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, docutils, gunicorn, mypy2
- [📄table](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base-mem.svg)
- [📄table](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.md)
- [📈time plot](bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9217931145)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.md)
- [📈time plot](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.56%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.md)
- [📈time plot](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.90%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dulwich_log, mypy2, sqlglot_normalize
- [📄table](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 94.77%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.md)
- [📈time plot](bm-20240523-pythonperf1-amd64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9217931145)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.md)
- [📈time plot](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.md)
- [📈time plot](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 90.81%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 90.11%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.md)
- [📈time plot](bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9217931145)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 0.80x
- missing benchmarks: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.md)
- [📈time plot](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.72x
- missing benchmarks: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.md)
- [📈time plot](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.66x
- missing benchmarks: aiohttp, bpe_tokeniser, dulwich_log, gunicorn, mypy2, sqlglot_normalize
- [📄table](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base-mem.svg)
- [📄table](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.md)
- [📈time plot](bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd-vs-base.svg)

