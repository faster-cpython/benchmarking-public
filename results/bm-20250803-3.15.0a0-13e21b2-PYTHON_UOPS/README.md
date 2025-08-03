# Results

- fork: python/13e21b2fd6343ba8309e
- version: 3.15.0a0
- config: T2
- commit hash: [13e21b2](https://github.com/python/cpython/commit/13e21b2)
- commit date: 2025-08-03T19:32:46+01:00
- commit merge base: [1612dcbafe763014deefd679fe75ac5831a14a43](https://github.com/python/cpython/commit/1612dcbafe763014deefd679fe75ac5831a14a43)
- ref: 13e21b2fd6343ba8309e

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16709235122)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2.json)

### vs. 3.10.4

- Geometric mean: 1.149x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2-vs-3.10.4.md)
- [📈time plot](bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x slower (HPT: reliability of 98.34%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2-vs-3.12.0.md)
- [📈time plot](bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.094x slower (HPT: reliability of 99.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2-vs-3.13.0.md)
- [📈time plot](bm-20250803-pythonperf2-x86_64-python-13e21b2fd6343ba8309e-3.15.0a0-13e21b2-vs-3.13.0.svg)

