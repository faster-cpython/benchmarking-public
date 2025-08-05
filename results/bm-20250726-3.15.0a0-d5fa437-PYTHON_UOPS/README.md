# Results

- fork: python/d5fa437dfb50e2e47632
- version: 3.15.0a0
- config: T2
- commit hash: [d5fa437](https://github.com/python/cpython/commit/d5fa437)
- commit date: 2025-07-26T22:14:12+05:30
- commit merge base: [d658b9053beaacaae80e318f59a5ddd672aa757a](https://github.com/python/cpython/commit/d658b9053beaacaae80e318f59a5ddd672aa757a)
- ref: d5fa437dfb50e2e47632

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16740364040)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437.json)

### vs. 3.10.4

- Geometric mean: 1.114x faster (HPT: reliability of 99.94%, 1.05x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437-vs-3.10.4.md)
- [📈time plot](bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.137x slower (HPT: reliability of 98.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437-vs-3.12.0.md)
- [📈time plot](bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.120x slower (HPT: reliability of 99.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437-vs-3.13.0.md)
- [📈time plot](bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437-vs-3.13.0.svg)

