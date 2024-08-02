# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [34e6994](https://github.com/brandtbucher/cpython/commit/34e6994)
- commit date: 2024-06-20T14:45:04-07:00
- commit merge base: [9f741e55c16376412c1473aa45b94314c00a0c43](https://github.com/brandtbucher/cpython/commit/9f741e55c16376412c1473aa45b94314c00a0c43)
- ref: justin_compact

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.md)
- [📈time plot](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.md)
- [📈time plot](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.63%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base-mem.svg)
- [📄table](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.md)
- [📈time plot](bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 97.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base-mem.svg)
- [📄table](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.md)
- [📈time plot](bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.md)
- [📈time plot](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 55.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.md)
- [📈time plot](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 94.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.07%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base-mem.svg)
- [📄table](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.md)
- [📈time plot](bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.md)
- [📈time plot](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.md)
- [📈time plot](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 98.55%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, sqlglot_normalize
- [📄table](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 82.40%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.md)
- [📈time plot](bm-20240620-pythonperf1-amd64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.md)
- [📈time plot](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.md)
- [📈time plot](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.32%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 97.74%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.md)
- [📈time plot](bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9605230925)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.md)
- [📈time plot](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.md)
- [📈time plot](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.md)
- [📈time plot](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 81.89%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base-mem.svg)
- [📄table](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.md)
- [📈time plot](bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994-vs-base.svg)

