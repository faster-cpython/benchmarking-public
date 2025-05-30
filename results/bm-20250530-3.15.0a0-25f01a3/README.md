# Results

- fork: zooba/gh_134923
- version: 3.15.0a0
- config: 
- commit hash: [25f01a3](https://github.com/zooba/cpython/commit/25f01a3)
- commit date: 2025-05-30T11:02:45+01:00
- commit merge base: [b367e27af9b52528e395f95b277ec7b69e98e287](https://github.com/python/cpython/commit/b367e27af9b52528e395f95b277ec7b69e98e287)
- ref: gh_134923

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15348561360)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3.json)

### vs. 3.10.4

- Geometric mean: 1.165x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-3.10.4.md)
- [📈time plot](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-3.12.0.md)
- [📈time plot](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x slower (HPT: reliability of 76.67%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-3.13.0.md)
- [📈time plot](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 77.38%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-base.md)
- [📈time plot](bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3-vs-base.svg)

