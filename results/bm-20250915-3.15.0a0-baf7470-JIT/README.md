# Results

- fork: python/baf747051557d029bc80
- version: 3.15.0a0
- config: JIT
- commit hash: [baf7470](https://github.com/python/cpython/commit/baf7470)
- commit date: 2025-09-15T12:01:33+03:00
- commit merge base: [097fc12149cbe7b336bdb3aad57e622de799611c](https://github.com/python/cpython/commit/097fc12149cbe7b336bdb3aad57e622de799611c)
- ref: baf747051557d029bc80

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17738836342)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470.json)

### vs. 3.10.4

- Geometric mean: 1.339x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470-vs-3.10.4.md)
- [📈time plot](bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470-vs-3.12.0.md)
- [📈time plot](bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470-vs-3.13.0.md)
- [📈time plot](bm-20250915-pythonperf2-x86_64-python-baf747051557d029bc80-3.15.0a0-baf7470-vs-3.13.0.svg)

