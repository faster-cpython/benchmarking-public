# Results

- fork: faster-cpython/check_periodic_at_en
- version: 3.15.0a0
- config: T2
- commit hash: [021fc09](https://github.com/faster%2dcpython/cpython/commit/021fc09)
- commit date: 2025-07-25T12:35:01+01:00
- commit merge base: [ae4d27eba7c746463c62649c36d53979f3a00f94](https://github.com/python/cpython/commit/ae4d27eba7c746463c62649c36d53979f3a00f94)
- ref: check_periodic_at_en

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16566210006)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09.json)

### vs. 3.10.4

- Geometric mean: 1.156x faster (HPT: reliability of 99.77%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.10.4.md)
- [📈time plot](bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x slower (HPT: reliability of 89.84%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.12.0.md)
- [📈time plot](bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x slower (HPT: reliability of 99.99%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.13.0.md)
- [📈time plot](bm-20250725-pythonperf1-amd64-faster%252dcpython-check_periodic_at_en-3.15.0a0-021fc09-vs-3.13.0.svg)

