# Results

- fork: brandtbucher
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [98575b4](https://github.com/brandtbucher/cpython/commit/98575b4)
- commit date: 2024-03-21T12:37:08-07:00
- commit merge base: [dcaf33a41d5d220523d71c9b35bc08f5b8405dac](https://github.com/brandtbucher/cpython/commit/dcaf33a41d5d220523d71c9b35bc08f5b8405dac)
- ref: justin_ghccc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8381067358)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.md)
- [📈time plot](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.20x slower (HPT: reliability of 98.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.md)
- [📈time plot](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.23x slower (HPT: reliability of 99.61%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.md)
- [📈time plot](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base-mem.png)
- [📄table](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.md)
- [📈time plot](bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8381067358)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.35
- [raw results](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.md)
- [📈time plot](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.18x slower (HPT: reliability of 99.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.md)
- [📈time plot](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.26x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.md)
- [📈time plot](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base-mem.png)
- [📄table](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.md)
- [📈time plot](bm-20240321-pythonperf2-x86_64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8381067358)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4.json)

### vs. 3.10.4

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.md)
- [📈time plot](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.14x slower (HPT: reliability of 65.23%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.md)
- [📈time plot](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.17x slower (HPT: reliability of 67.10%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.md)
- [📈time plot](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 91.18%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.md)
- [📈time plot](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.png)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8381067358)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4.json)

### vs. 3.10.4

- Geometric mean: 1.02x faster (HPT: reliability of 99.88%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.md)
- [📈time plot](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.88%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.md)
- [📈time plot](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.91%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.md)
- [📈time plot](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.06x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.md)
- [📈time plot](bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8381067358)
- cpu model: missing
- platform: macOS-14.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4.json)

### vs. 3.10.4

- Geometric mean: 1.02x faster (HPT: reliability of 99.72%, 1.01x faster at 99th %ile)
- Memory usage: 1.60x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.md)
- [📈time plot](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.30x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.48x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg
- [📄table](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.md)
- [📈time plot](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.26x slower (HPT: reliability of 99.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.md)
- [📈time plot](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 92.85%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base-mem.png)
- [📄table](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.md)
- [📈time plot](bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-base.png)

