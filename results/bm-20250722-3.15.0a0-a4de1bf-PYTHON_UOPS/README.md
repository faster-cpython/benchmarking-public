# Results

- fork: faster-cpython/tier_2_tos_caching
- version: 3.15.0a0
- config: T2
- commit hash: [a4de1bf](https://github.com/faster%2dcpython/cpython/commit/a4de1bf)
- commit date: 2025-07-22T13:49:45+01:00
- commit merge base: [9c7b2af73dee2b99793637c3b70f724641b84349](https://github.com/python/cpython/commit/9c7b2af73dee2b99793637c3b70f724641b84349)
- ref: tier_2_tos_caching

## linux x86_64 (azure)

- [pystats raw](bm-20250722-azure-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-pystats.json)
- [pystats table](bm-20250722-azure-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16468733899)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250722-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json)

### vs. 3.10.4

- Geometric mean: 1.108x faster (HPT: reliability of 99.92%, 1.04x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250722-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-vs-3.10.4.md)
- [📈time plot](bm-20250722-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.142x slower (HPT: reliability of 99.34%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250722-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-vs-3.12.0.md)
- [📈time plot](bm-20250722-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.125x slower (HPT: reliability of 99.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250722-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-vs-3.13.0.md)
- [📈time plot](bm-20250722-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf-vs-3.13.0.svg)

