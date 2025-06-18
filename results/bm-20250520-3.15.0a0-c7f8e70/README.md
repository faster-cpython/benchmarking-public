# Results

- fork: python/c7f8e706e116d7986da4
- version: 3.15.0a0
- config: 
- commit hash: [c7f8e70](https://github.com/python/cpython/commit/c7f8e70)
- commit date: 2025-05-20T12:30:00-07:00
- commit merge base: [91e6a58e2d6fd23e886135457e28dfa980ec49ed](https://github.com/python/cpython/commit/91e6a58e2d6fd23e886135457e28dfa980ec49ed)
- ref: c7f8e706e116d7986da4

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15714424463)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70.json)

### vs. 3.10.4

- Geometric mean: 1.443x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-3.10.4.md)
- [📈time plot](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-3.12.0.md)
- [📈time plot](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 97.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-3.13.0.md)
- [📈time plot](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 99.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-base-mem.svg)
- [📄table](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-base.md)
- [📈time plot](bm-20250520-linux-x86_64-python-c7f8e706e116d7986da4-3.15.0a0-c7f8e70-vs-base.svg)

