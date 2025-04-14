# Results

- fork: mdboom/tuple_hash_cache_emp
- version: 3.14.0a6+
- config: 
- commit hash: [40ad9fc](https://github.com/mdboom/cpython/commit/40ad9fc)
- commit date: 2025-03-21T08:49:24-04:00
- commit merge base: [ce79274e9f093bd06d2285c9af48dbcbc92173de](https://github.com/python/cpython/commit/ce79274e9f093bd06d2285c9af48dbcbc92173de)
- ref: tuple_hash_cache_emp

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13992120783)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc.json)

### vs. 3.10.4

- Geometric mean: 1.320x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-3.10.4.md)
- [📈time plot](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x faster (HPT: reliability of 52.27%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-3.12.0.md)
- [📈time plot](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-3.13.0.md)
- [📈time plot](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 99.30%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 thrift
- [🧠memory plot](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-base-mem.svg)
- [📄table](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-base.md)
- [📈time plot](bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6%2B-40ad9fc-vs-base.svg)

