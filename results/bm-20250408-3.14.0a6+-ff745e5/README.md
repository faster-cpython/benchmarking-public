# Results

- fork: mdboom/unicode_hash_eq
- version: 3.14.0a6+
- config: 
- commit hash: [ff745e5](https://github.com/mdboom/cpython/commit/ff745e5)
- commit date: 2025-04-08T14:24:46-04:00
- commit merge base: [3b3720f1a26ab34377542b48eb6a6565f78ff892](https://github.com/python/cpython/commit/3b3720f1a26ab34377542b48eb6a6565f78ff892)
- ref: unicode_hash_eq

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14340873020)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5.json)

### vs. 3.10.4

- Geometric mean: 1.457x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-3.10.4.md)
- [📈time plot](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-3.12.0.md)
- [📈time plot](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-3.13.0.md)
- [📈time plot](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 99.72%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-base-mem.svg)
- [📄table](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-base.md)
- [📈time plot](bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6%2B-ff745e5-vs-base.svg)

