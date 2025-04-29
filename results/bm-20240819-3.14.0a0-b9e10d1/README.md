# Results

- fork: python/b9e10d1a0fc4d8428d4b
- version: 3.14.0a0
- config: 
- commit hash: [b9e10d1](https://github.com/python/cpython/commit/b9e10d1)
- commit date: 2024-08-19T07:51:38+00:00
- commit merge base: [be257c58152e9b960827362b11c9ef2223fd6267](https://github.com/python/cpython/commit/be257c58152e9b960827362b11c9ef2223fd6267)
- ref: b9e10d1a0fc4d8428d4b

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14715516915)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20240819-linux-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1.json)

### vs. 3.10.4

- Geometric mean: 1.396x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20240819-linux-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.10.4.md)
- [📈time plot](bm-20240819-linux-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20240819-linux-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.12.0.md)
- [📈time plot](bm-20240819-linux-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 82.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, dulwich_log, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20240819-linux-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.13.0.md)
- [📈time plot](bm-20240819-linux-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.13.0.svg)

