# Results

- fork: mdboom/msvc_musttail_aa
- version: 3.14.0a5+
- config: 
- commit hash: [90d131f](https://github.com/mdboom/cpython/commit/90d131f)
- commit date: 2025-03-10T19:23:31-04:00
- commit merge base: [f963239ff1f986742d4c6bab2ab7b73f5a4047f6](https://github.com/python/cpython/commit/f963239ff1f986742d4c6bab2ab7b73f5a4047f6)
- ref: msvc_musttail_aa

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13776861299)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f.json)

### vs. 3.10.4

- Geometric mean: 1.167x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-3.10.4.md)
- [📈time plot](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.290x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-3.12.0.md)
- [📈time plot](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.301x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-3.13.0.md)
- [📈time plot](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.301x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-base.md)
- [📈time plot](bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5%2B-90d131f-vs-base.svg)

