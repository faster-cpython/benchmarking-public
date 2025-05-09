# Results

- fork: brandtbucher/load_const_borrow
- version: 3.15.0a0
- config: JIT
- commit hash: [60413da](https://github.com/brandtbucher/cpython/commit/60413da)
- commit date: 2025-05-08T16:14:43-07:00
- commit merge base: [c492ac72525ea5887082ee991b45cc237cd02a40](https://github.com/python/cpython/commit/c492ac72525ea5887082ee991b45cc237cd02a40)
- ref: load_const_borrow

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14917916222)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da-vs-3.10.4.md)
- [📈time plot](bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da-vs-3.12.0.md)
- [📈time plot](bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x slower (HPT: reliability of 99.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da-vs-3.13.0.md)
- [📈time plot](bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da-vs-3.13.0.svg)

