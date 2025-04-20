# Results

- fork: python/71da68d5887b6c058907
- version: 3.14.0a7+
- config: JIT
- commit hash: [71da68d](https://github.com/python/cpython/commit/71da68d)
- commit date: 2025-04-19T18:11:21+00:00
- commit merge base: [e7c5f60efc149dda3d3592fa2001f4583b128512](https://github.com/python/cpython/commit/e7c5f60efc149dda3d3592fa2001f4583b128512)
- ref: 71da68d5887b6c058907

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.311x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 97.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 92.01%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.026x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.296x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 74.66%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 78.81%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.069x faster (HPT: reliability of 92.78%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.091x faster (HPT: reliability of 99.92%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.098x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-pythonperf1_win32-x86-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.399x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.099x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.152x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

