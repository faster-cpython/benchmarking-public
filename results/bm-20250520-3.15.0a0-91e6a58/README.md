# Results

- fork: python/91e6a58e2d6fd23e8861
- version: 3.15.0a0
- config: 
- commit hash: [91e6a58](https://github.com/python/cpython/commit/91e6a58)
- commit date: 2025-05-20T18:41:14+00:00
- commit merge base: [3b7888bf3d43b903f0a7ebd16f39d8bb61dfbb9e](https://github.com/python/cpython/commit/3b7888bf3d43b903f0a7ebd16f39d8bb61dfbb9e)
- ref: 91e6a58e2d6fd23e8861

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15714424463)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250520-linux-x86_64-python-91e6a58e2d6fd23e8861-3.15.0a0-91e6a58.json)

### vs. 3.10.4

- Geometric mean: 1.452x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250520-linux-x86_64-python-91e6a58e2d6fd23e8861-3.15.0a0-91e6a58-vs-3.10.4.md)
- [📈time plot](bm-20250520-linux-x86_64-python-91e6a58e2d6fd23e8861-3.15.0a0-91e6a58-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250520-linux-x86_64-python-91e6a58e2d6fd23e8861-3.15.0a0-91e6a58-vs-3.12.0.md)
- [📈time plot](bm-20250520-linux-x86_64-python-91e6a58e2d6fd23e8861-3.15.0a0-91e6a58-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250520-linux-x86_64-python-91e6a58e2d6fd23e8861-3.15.0a0-91e6a58-vs-3.13.0.md)
- [📈time plot](bm-20250520-linux-x86_64-python-91e6a58e2d6fd23e8861-3.15.0a0-91e6a58-vs-3.13.0.svg)

