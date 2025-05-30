# Results

- fork: python/1a89991d2362867a9127
- version: 3.15.0a0
- config: 
- commit hash: [1a89991](https://github.com/python/cpython/commit/1a89991)
- commit date: 2025-05-30T15:52:36+00:00
- commit merge base: [52deabefd0af8fc6d9b40823323437bf210f50a5](https://github.com/python/cpython/commit/52deabefd0af8fc6d9b40823323437bf210f50a5)
- ref: 1a89991d2362867a9127

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15354602275)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991-vs-3.10.4.md)
- [📈time plot](bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991-vs-3.12.0.md)
- [📈time plot](bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x slower (HPT: reliability of 99.74%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991-vs-3.13.0.md)
- [📈time plot](bm-20250530-linux-x86_64-python-1a89991d2362867a9127-3.15.0a0-1a89991-vs-3.13.0.svg)

