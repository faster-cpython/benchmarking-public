# Results

- fork: python/a269e691de91fcc09827
- version: 3.15.0a0
- config: JIT
- commit hash: [a269e69](https://github.com/python/cpython/commit/a269e69)
- commit date: 2025-09-18T14:12:07+01:00
- commit merge base: [243d599a05e88739f4ee8486fc76e382020174e4](https://github.com/python/cpython/commit/243d599a05e88739f4ee8486fc76e382020174e4)
- ref: a269e691de91fcc09827

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18617918911)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250918-pythonperf2-x86_64-python-a269e691de91fcc09827-3.15.0a0-a269e69.json)

### vs. 3.10.4

- Geometric mean: 1.336x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250918-pythonperf2-x86_64-python-a269e691de91fcc09827-3.15.0a0-a269e69-vs-3.10.4.md)
- [📈time plot](bm-20250918-pythonperf2-x86_64-python-a269e691de91fcc09827-3.15.0a0-a269e69-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250918-pythonperf2-x86_64-python-a269e691de91fcc09827-3.15.0a0-a269e69-vs-3.12.0.md)
- [📈time plot](bm-20250918-pythonperf2-x86_64-python-a269e691de91fcc09827-3.15.0a0-a269e69-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250918-pythonperf2-x86_64-python-a269e691de91fcc09827-3.15.0a0-a269e69-vs-3.13.0.md)
- [📈time plot](bm-20250918-pythonperf2-x86_64-python-a269e691de91fcc09827-3.15.0a0-a269e69-vs-3.13.0.svg)

