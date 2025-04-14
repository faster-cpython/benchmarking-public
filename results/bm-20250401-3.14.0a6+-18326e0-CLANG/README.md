# Results

- fork: mdboom/msvc_musttail_clang_
- version: 3.14.0a6+
- config: 
- commit hash: [18326e0](https://github.com/mdboom/cpython/commit/18326e0)
- commit date: 2025-04-01T10:09:15-04:00
- commit merge base: [3b3720f1a26ab34377542b48eb6a6565f78ff892](https://github.com/python/cpython/commit/3b3720f1a26ab34377542b48eb6a6565f78ff892)
- ref: msvc_musttail_clang_

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14197879081)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6%2B-18326e0.json)

### vs. 3.10.4

- Geometric mean: 1.479x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6%2B-18326e0-vs-3.10.4.md)
- [📈time plot](bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6%2B-18326e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.256x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6%2B-18326e0-vs-3.12.0.md)
- [📈time plot](bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6%2B-18326e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.171x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6%2B-18326e0-vs-3.13.0.md)
- [📈time plot](bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6%2B-18326e0-vs-3.13.0.svg)

