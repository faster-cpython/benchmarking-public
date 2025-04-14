# Results

- fork: mdboom/tuple_hash_cache
- version: 3.14.0a6+
- config: 
- commit hash: [bd82b00](https://github.com/mdboom/cpython/commit/bd82b00)
- commit date: 2025-03-19T11:35:25-04:00
- commit merge base: [f81990024554a75e2ab31133a72d9f0954690435](https://github.com/python/cpython/commit/f81990024554a75e2ab31133a72d9f0954690435)
- ref: tuple_hash_cache

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13950573141)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00.json)

### vs. 3.10.4

- Geometric mean: 1.309x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-3.10.4.md)
- [📈time plot](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x faster (HPT: reliability of 59.01%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-3.12.0.md)
- [📈time plot](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 97.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-3.13.0.md)
- [📈time plot](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-base-mem.svg)
- [📄table](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-base.md)
- [📈time plot](bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6%2B-bd82b00-vs-base.svg)

