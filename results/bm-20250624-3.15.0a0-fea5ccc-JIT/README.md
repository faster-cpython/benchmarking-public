# Results

- fork: python/fea5ccc55d8486300beb
- version: 3.15.0a0
- config: JIT
- commit hash: [fea5ccc](https://github.com/python/cpython/commit/fea5ccc)
- commit date: 2025-06-24T10:02:50-07:00
- commit merge base: [b3ab94acd308591bbdf264f1722fedc7ee25d6fa](https://github.com/python/cpython/commit/b3ab94acd308591bbdf264f1722fedc7ee25d6fa)
- ref: fea5ccc55d8486300beb

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15863485524)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc.json)

### vs. 3.10.4

- Geometric mean: 1.470x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc-vs-3.10.4.md)
- [📈time plot](bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc-vs-3.12.0.md)
- [📈time plot](bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.054x faster (HPT: reliability of 99.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc-vs-3.13.0.md)
- [📈time plot](bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc-vs-3.13.0.svg)

