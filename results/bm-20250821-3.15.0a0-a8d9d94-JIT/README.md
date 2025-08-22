# Results

- fork: python/a8d9d947843200a09c15
- version: 3.15.0a0
- config: JIT
- commit hash: [a8d9d94](https://github.com/python/cpython/commit/a8d9d94)
- commit date: 2025-08-21T10:40:53+01:00
- commit merge base: [c056a089d8573b03c62d52ee05f48bf6804da66b](https://github.com/python/cpython/commit/c056a089d8573b03c62d52ee05f48bf6804da66b)
- ref: a8d9d947843200a09c15

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17150126139)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.md)
- [📈time plot](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.md)
- [📈time plot](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.089x faster (HPT: reliability of 95.77%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.md)
- [📈time plot](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.svg)

