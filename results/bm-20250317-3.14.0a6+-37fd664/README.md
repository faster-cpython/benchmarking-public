# Results

- fork: mdboom/reorg_pyinterpreterf
- version: 3.14.0a6+
- config: 
- commit hash: [37fd664](https://github.com/mdboom/cpython/commit/37fd664)
- commit date: 2025-03-17T13:57:00-04:00
- commit merge base: [bb0268f60dfe903a9bdb8d84104247a9318c6b18](https://github.com/python/cpython/commit/bb0268f60dfe903a9bdb8d84104247a9318c6b18)
- ref: reorg_pyinterpreterf

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13906499897)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664.json)

### vs. 3.10.4

- Geometric mean: 1.316x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-3.10.4.md)
- [📈time plot](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 70.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-3.12.0.md)
- [📈time plot](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-3.13.0.md)
- [📈time plot](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 63.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-base-mem.svg)
- [📄table](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-base.md)
- [📈time plot](bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6%2B-37fd664-vs-base.svg)

