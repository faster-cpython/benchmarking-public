# Results

- fork: python/9fbd66a93d526c49fac8
- version: 3.15.0a0
- config: JIT
- commit hash: [9fbd66a](https://github.com/python/cpython/commit/9fbd66a)
- commit date: 2025-05-28T19:03:41+01:00
- commit merge base: [f6324bc7eedc615c3c961fe368a8c56697d42936](https://github.com/python/cpython/commit/f6324bc7eedc615c3c961fe368a8c56697d42936)
- ref: 9fbd66a93d526c49fac8

## linux x86_64 (azure)

- [pystats raw](bm-20250528-azure-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-pystats.json)
- [pystats table](bm-20250528-azure-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15313746480)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a.json)

### vs. 3.10.4

- Geometric mean: 1.913x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-vs-3.10.4.md)
- [📈time plot](bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.590x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-vs-3.12.0.md)
- [📈time plot](bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.353x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-vs-3.13.0.md)
- [📈time plot](bm-20250528-linux-x86_64-python-9fbd66a93d526c49fac8-3.15.0a0-9fbd66a-vs-3.13.0.svg)

