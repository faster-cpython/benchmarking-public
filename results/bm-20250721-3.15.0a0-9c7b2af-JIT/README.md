# Results

- fork: python/9c7b2af73dee2b997936
- version: 3.15.0a0
- config: JIT
- commit hash: [9c7b2af](https://github.com/python/cpython/commit/9c7b2af)
- commit date: 2025-07-21T11:17:36+02:00
- commit merge base: [cf19b6435d02dd7be11b84a44f4a8a9f1a935b15](https://github.com/python/cpython/commit/cf19b6435d02dd7be11b84a44f4a8a9f1a935b15)
- ref: 9c7b2af73dee2b997936

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16413910315)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af.json)

### vs. 3.10.4

- Geometric mean: 1.318x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af-vs-3.10.4.md)
- [📈time plot](bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af-vs-3.12.0.md)
- [📈time plot](bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.079x faster (HPT: reliability of 87.97%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af-vs-3.13.0.md)
- [📈time plot](bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af-vs-3.13.0.svg)

