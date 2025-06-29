# Results

- fork: python/5334732f9c8a44722e4b
- version: 3.15.0a0
- config: JIT
- commit hash: [5334732](https://github.com/python/cpython/commit/5334732)
- commit date: 2025-06-28T14:11:31+01:00
- commit merge base: [579acf45629fa0b7787ec78fa4049fc6a6388b71](https://github.com/python/cpython/commit/579acf45629fa0b7787ec78fa4049fc6a6388b71)
- ref: 5334732f9c8a44722e4b

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.201x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x slower (HPT: reliability of 99.79%, 1.01x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.054x slower (HPT: reliability of 99.90%, 1.01x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 76.44%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

