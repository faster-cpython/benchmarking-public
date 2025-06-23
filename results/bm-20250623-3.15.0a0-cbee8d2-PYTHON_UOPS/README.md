# Results

- fork: faster-cpython/tier_2_tos_caching
- version: 3.15.0a0
- config: T2
- commit hash: [cbee8d2](https://github.com/faster%2dcpython/cpython/commit/cbee8d2)
- commit date: 2025-06-23T10:11:56+01:00
- commit merge base: [c825b5d989d2e796b48e10230447c616e19c3d67](https://github.com/python/cpython/commit/c825b5d989d2e796b48e10230447c616e19c3d67)
- ref: tier_2_tos_caching

## linux x86_64 (azure)

- [pystats raw](bm-20250623-azure-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-pystats.json)
- [pystats table](bm-20250623-azure-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15820181172)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250623-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2.json)

### vs. 3.10.4

- Geometric mean: 1.266x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-vs-3.10.4.md)
- [📈time plot](bm-20250623-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x slower (HPT: reliability of 88.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250623-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-vs-3.12.0.md)
- [📈time plot](bm-20250623-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.085x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-vs-3.13.0.md)
- [📈time plot](bm-20250623-linux-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2-vs-3.13.0.svg)

