# Results

- fork: python/425f60b9eb253c57bc32
- version: 3.14.0a6+
- config: TAILCALL
- commit hash: [425f60b](https://github.com/python/cpython/commit/425f60b)
- commit date: 2025-03-29T21:15:48+00:00
- commit merge base: [c6b1a073438d93d4e62957accc73487df6711851](https://github.com/python/cpython/commit/c6b1a073438d93d4e62957accc73487df6711851)
- ref: 425f60b9eb253c57bc32

## linux aarch64 (arminc_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14150598282)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b.json)

### vs. 3.10.4

- [📄table](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.md)
- [📈time plot](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.md)
- [📈time plot](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.md)
- [📈time plot](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base-mem.svg)
- [📄table](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.md)
- [📈time plot](bm-20250329-arminc_clang-aarch64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.svg)

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14150598282)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b.json)

### vs. 3.10.4

- [📄table](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.md)
- [📈time plot](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.md)
- [📈time plot](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.md)
- [📈time plot](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base-mem.svg)
- [📄table](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.md)
- [📈time plot](bm-20250329-linux_clang-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14150598282)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b.json)

### vs. 3.10.4

- Geometric mean: 1.398x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.md)
- [📈time plot](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.md)
- [📈time plot](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.md)
- [📈time plot](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base-mem.svg)
- [📄table](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.md)
- [📈time plot](bm-20250329-pythonperf2-x86_64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14171599912)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b.json)

### vs. base

- Geometric mean: 1.166x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.md)
- [📈time plot](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.md)
- [📈time plot](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.md)
- [📈time plot](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.md)
- [📈time plot](bm-20250329-pythonperf1_clang-amd64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14150598282)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b.json)

### vs. 3.10.4

- [📄table](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.md)
- [📈time plot](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.md)
- [📈time plot](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.md)
- [📈time plot](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base-mem.svg)
- [📄table](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.md)
- [📈time plot](bm-20250329-darwin_clang-arm64-python-425f60b9eb253c57bc32-3.14.0a6%2B-425f60b-vs-base.svg)

