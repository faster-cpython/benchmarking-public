# Results

- fork: python/1a87b6e9ae6da255f304
- version: 3.15.0a0
- config: TAILCALL
- commit hash: [1a87b6e](https://github.com/python/cpython/commit/1a87b6e)
- commit date: 2025-05-10T22:37:17+00:00
- commit merge base: [dc191d248456855d228b09f0e0206e0b656f113c](https://github.com/python/cpython/commit/dc191d248456855d228b09f0e0206e0b656f113c)
- ref: 1a87b6e9ae6da255f304

## linux aarch64 (arminc_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- [📄table](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-arminc_clang-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- [📄table](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-linux_clang-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- Geometric mean: 1.395x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, djangocms, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 99.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, djangocms, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- [🧠memory plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- [📄table](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-pythonperf1_clang-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- [📄table](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-darwin_clang-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

