# Results

- fork: python/main
- version: 3.15.0a0
- config: JIT
- commit hash: [3ec3d05](https://github.com/python/cpython/commit/3ec3d05)
- commit date: 2025-08-03T19:53:01-07:00
- commit merge base: [b266fbc9ecd25d08ab572ecb91913e86b6ddc75e](https://github.com/python/cpython/commit/b266fbc9ecd25d08ab572ecb91913e86b6ddc75e)
- ref: main

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16714251114)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05.json)

### vs. 3.10.4

- Geometric mean: 1.332x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-3.10.4.md)
- [📈time plot](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-3.12.0.md)
- [📈time plot](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-3.13.0.md)
- [📈time plot](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 69.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-base-mem.svg)
- [📄table](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-base.md)
- [📈time plot](bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05-vs-base.svg)

