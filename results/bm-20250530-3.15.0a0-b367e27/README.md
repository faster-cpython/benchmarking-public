# Results

- fork: python/b367e27af9b52528e395
- version: 3.15.0a0
- config: 
- commit hash: [b367e27](https://github.com/python/cpython/commit/b367e27)
- commit date: 2025-05-30T17:59:23+09:00
- commit merge base: [2f2bee21118adce653ee5bc4eb31d30327465966](https://github.com/python/cpython/commit/2f2bee21118adce653ee5bc4eb31d30327465966)
- ref: b367e27af9b52528e395

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15348561360)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27.json)

### vs. 3.10.4

- Geometric mean: 1.166x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27-vs-3.10.4.md)
- [📈time plot](bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.068x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27-vs-3.12.0.md)
- [📈time plot](bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x slower (HPT: reliability of 88.54%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27-vs-3.13.0.md)
- [📈time plot](bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27-vs-3.13.0.svg)

