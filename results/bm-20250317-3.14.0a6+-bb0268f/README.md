# Results

- fork: python/bb0268f60dfe903a9bdb
- version: 3.14.0a6+
- config: 
- commit hash: [bb0268f](https://github.com/python/cpython/commit/bb0268f)
- commit date: 2025-03-17T14:55:02+01:00
- commit merge base: [978e37bb5f979cccce36613637ac2d94b43c71b2](https://github.com/python/cpython/commit/978e37bb5f979cccce36613637ac2d94b43c71b2)
- ref: bb0268f60dfe903a9bdb

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13906499897)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6%2B-bb0268f.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6%2B-bb0268f-vs-3.10.4.md)
- [📈time plot](bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6%2B-bb0268f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.019x faster (HPT: reliability of 75.45%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6%2B-bb0268f-vs-3.12.0.md)
- [📈time plot](bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6%2B-bb0268f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6%2B-bb0268f-vs-3.13.0.md)
- [📈time plot](bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6%2B-bb0268f-vs-3.13.0.svg)

