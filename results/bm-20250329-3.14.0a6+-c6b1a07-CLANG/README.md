# Results

- fork: python/c6b1a073438d93d4e629
- version: 3.14.0a6+
- config: CLANG
- commit hash: [c6b1a07](https://github.com/python/cpython/commit/c6b1a07)
- commit date: 2025-03-29T19:14:37+02:00
- commit merge base: [fccf9ab33d0b16e6171c533d139b6118503197c1](https://github.com/python/cpython/commit/fccf9ab33d0b16e6171c533d139b6118503197c1)
- ref: c6b1a073438d93d4e629

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14171599912)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6%2B-c6b1a07.json)

### vs. 3.10.4

- Geometric mean: 1.489x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6%2B-c6b1a07-vs-3.10.4.md)
- [📈time plot](bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6%2B-c6b1a07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.265x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6%2B-c6b1a07-vs-3.12.0.md)
- [📈time plot](bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6%2B-c6b1a07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.180x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6%2B-c6b1a07-vs-3.13.0.md)
- [📈time plot](bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6%2B-c6b1a07-vs-3.13.0.svg)

