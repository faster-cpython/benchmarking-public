# Results

- fork: python/71da68d5887b6c058907
- version: 3.14.0a7+
- config: NOGIL
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

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x slower (HPT: reliability of 99.82%, 1.01x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x slower (HPT: reliability of 99.87%, 1.01x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.123x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.253x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x slower (HPT: reliability of 99.90%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 97.41%, 1.00x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-pythonperf2-x86_64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.142x faster (HPT: reliability of 99.89%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 97.47%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x slower (HPT: reliability of 99.97%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.115x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14554018167)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d.json)

### vs. 3.10.4

- Geometric mean: 1.367x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.091x faster (HPT: reliability of 98.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.140x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- [🧠memory plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base-mem.svg)
- [📄table](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.md)
- [📈time plot](bm-20250419-darwin-arm64-python-71da68d5887b6c058907-3.14.0a7%2B-71da68d-vs-base.svg)

