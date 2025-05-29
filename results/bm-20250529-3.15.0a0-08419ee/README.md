# Results

- fork: faster-cpython/specialize_for_iter_
- version: 3.15.0a0
- config: 
- commit hash: [08419ee](https://github.com/faster%2dcpython/cpython/commit/08419ee)
- commit date: 2025-05-29T09:30:40+01:00
- commit merge base: [f6f4e8a6622d556641799b02aed7ac018d878cdc](https://github.com/python/cpython/commit/f6f4e8a6622d556641799b02aed7ac018d878cdc)
- ref: specialize_for_iter_

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15319753816)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee.json)

### vs. 3.10.4

- Geometric mean: 1.299x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-3.10.4.md)
- [📈time plot](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-3.12.0.md)
- [📈time plot](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 99.80%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-3.13.0.md)
- [📈time plot](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 93.46%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-base-mem.svg)
- [📄table](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-base.md)
- [📈time plot](bm-20250529-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-08419ee-vs-base.svg)

