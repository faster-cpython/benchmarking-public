# Results

- fork: mdboom/tuple_hash_cache2
- version: 3.14.0a6+
- config: 
- commit hash: [54e07d1](https://github.com/mdboom/cpython/commit/54e07d1)
- commit date: 2025-03-20T16:26:06-04:00
- commit merge base: [6146295a5b8e9286ccb8f90818b764c9a0192090](https://github.com/python/cpython/commit/6146295a5b8e9286ccb8f90818b764c9a0192090)
- ref: tuple_hash_cache2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13978995572)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1.json)

### vs. 3.10.4

- Geometric mean: 1.446x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-3.10.4.md)
- [📈time plot](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-3.12.0.md)
- [📈time plot](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-3.13.0.md)
- [📈time plot](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 99.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 thrift
- [🧠memory plot](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-base-mem.svg)
- [📄table](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-base.md)
- [📈time plot](bm-20250320-linux-x86_64-mdboom-tuple_hash_cache2-3.14.0a6%2B-54e07d1-vs-base.svg)

