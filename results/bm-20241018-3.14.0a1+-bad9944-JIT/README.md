# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [bad9944](https://github.com/brandtbucher/cpython/commit/bad9944)
- commit date: 2024-10-18T10:02:10-07:00
- commit merge base: [d8c864816121547338efa43c56e3f75ead98a924](https://github.com/brandtbucher/cpython/commit/d8c864816121547338efa43c56e3f75ead98a924)
- ref: justin_likely

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 99.97%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.md)
- [📈time plot](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.md)
- [📈time plot](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.md)
- [📈time plot](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 83.38%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base-mem.svg)
- [📄table](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.md)
- [📈time plot](bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.md)
- [📈time plot](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.md)
- [📈time plot](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.15%, 1.00x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.md)
- [📈time plot](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base-mem.svg)
- [📄table](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.md)
- [📈time plot](bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.md)
- [📈time plot](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x slower (HPT: reliability of 67.41%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.md)
- [📈time plot](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 66.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.md)
- [📈time plot](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.44%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base-mem.svg)
- [📄table](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.md)
- [📈time plot](bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.md)
- [📈time plot](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 54.72%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.md)
- [📈time plot](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.md)
- [📈time plot](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.23%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.md)
- [📈time plot](bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.md)
- [📈time plot](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.md)
- [📈time plot](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 99.39%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, sphinx, unpack_sequence
- [📄table](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.md)
- [📈time plot](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 60.24%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.md)
- [📈time plot](bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 98.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: sphinx, unpack_sequence
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 79.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base-mem.svg)
- [📄table](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.md)
- [📈time plot](bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1%2B-bad9944-vs-base.svg)

