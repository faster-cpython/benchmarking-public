# Results

- fork: python/71da68d5887b6c058907
- version: 3.14.0a7+
- config: TAILCALL
- commit hash: [71da68d](https://github.com/python/cpython/commit/71da68d)
- commit date: 2025-04-19T18:11:21+00:00
- commit merge base: [e7c5f60efc149dda3d3592fa2001f4583b128512](https://github.com/python/cpython/commit/e7c5f60efc149dda3d3592fa2001f4583b128512)
- ref: 71da68d5887b6c058907

## linux aarch64 (arminc_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- [📄table](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-arminc_clang-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- [📄table](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-linux_clang-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.417x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.035x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- [📄table](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-pythonperf1_clang-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- [📄table](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-darwin_clang-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

