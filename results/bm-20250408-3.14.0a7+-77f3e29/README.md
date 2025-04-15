# Results

- fork: eendebakpt/list_freelist_plus
- version: 3.14.0a7+
- config: 
- commit hash: [77f3e29](https://github.com/eendebakpt/cpython/commit/77f3e29)
- commit date: 2025-04-08T22:49:01+02:00
- commit merge base: [f5f1ac84b3b9d688b9e7d5943c975904b6b74513](https://github.com/python/cpython/commit/f5f1ac84b3b9d688b9e7d5943c975904b6b74513)
- ref: list_freelist_plus

## linux x86_64 (azure)

- [pystats raw](bm-20250408-azure-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-pystats.json)
- [pystats table](bm-20250408-azure-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-pystats.md)

### vs. base

- [pystats diff](bm-20250408-azure-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14456172465)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29.json)

### vs. 3.10.4

- Geometric mean: 1.474x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.10.4.md)
- [📈time plot](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.137x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.12.0.md)
- [📈time plot](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.13.0.md)
- [📈time plot](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 99.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-base-mem.svg)
- [📄table](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-base.md)
- [📈time plot](bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7%2B-77f3e29-vs-base.svg)

