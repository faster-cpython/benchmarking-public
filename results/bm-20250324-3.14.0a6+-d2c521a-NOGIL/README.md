# Results

- fork: mdboom/tuple_hash_cache2
- version: 3.14.0a6+
- config: NOGIL
- commit hash: [d2c521a](https://github.com/mdboom/cpython/commit/d2c521a)
- commit date: 2025-03-24T10:25:53-04:00
- commit merge base: [6226edc48baa888b413f1825b992d75921bd27fc](https://github.com/python/cpython/commit/6226edc48baa888b413f1825b992d75921bd27fc)
- ref: tuple_hash_cache2

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14038046396)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a.json)

### vs. 3.10.4

- Geometric mean: 1.214x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.57x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-3.10.4.md)
- [📈time plot](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x slower (HPT: reliability of 99.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-3.12.0.md)
- [📈time plot](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x slower (HPT: reliability of 99.34%, 1.00x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-3.13.0.md)
- [📈time plot](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 54.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 thrift
- [🧠memory plot](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-base-mem.svg)
- [📄table](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-base.md)
- [📈time plot](bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-d2c521a-vs-base.svg)

