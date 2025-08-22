# Results

- fork: python/f278afcabf1a1c4162a0
- version: 3.15.0a0
- config: JIT
- commit hash: [f278afc](https://github.com/python/cpython/commit/f278afc)
- commit date: 2025-08-22T12:28:33-04:00
- commit merge base: [b9bcd02e9fe976e0a6a8e8a0b336d598b1d73b13](https://github.com/python/cpython/commit/b9bcd02e9fe976e0a6a8e8a0b336d598b1d73b13)
- ref: f278afcabf1a1c4162a0

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17163134784)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json)

### vs. 3.10.4

- Geometric mean: 1.351x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc-vs-3.10.4.md)
- [📈time plot](bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.153x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc-vs-3.12.0.md)
- [📈time plot](bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.107x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc-vs-3.13.0.md)
- [📈time plot](bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc-vs-3.13.0.svg)

