# Results

- fork: python/b0e1c51882e3a129d1e4
- version: 3.14.0a0
- config: 
- commit hash: [b0e1c51](https://github.com/python/cpython/commit/b0e1c51)
- commit date: 2024-06-24T07:18:46-06:00
- commit merge base: [ac61d58db0753a3b37de21dbc6e86b38f2a93f1b](https://github.com/python/cpython/commit/ac61d58db0753a3b37de21dbc6e86b38f2a93f1b)
- ref: b0e1c51882e3a129d1e4

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14715515075)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20240624-linux-x86_64-python-b0e1c51882e3a129d1e4-3.14.0a0-b0e1c51.json)

### vs. 3.10.4

- Geometric mean: 1.395x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20240624-linux-x86_64-python-b0e1c51882e3a129d1e4-3.14.0a0-b0e1c51-vs-3.10.4.md)
- [📈time plot](bm-20240624-linux-x86_64-python-b0e1c51882e3a129d1e4-3.14.0a0-b0e1c51-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20240624-linux-x86_64-python-b0e1c51882e3a129d1e4-3.14.0a0-b0e1c51-vs-3.12.0.md)
- [📈time plot](bm-20240624-linux-x86_64-python-b0e1c51882e3a129d1e4-3.14.0a0-b0e1c51-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x slower (HPT: reliability of 91.84%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20240624-linux-x86_64-python-b0e1c51882e3a129d1e4-3.14.0a0-b0e1c51-vs-3.13.0.md)
- [📈time plot](bm-20240624-linux-x86_64-python-b0e1c51882e3a129d1e4-3.14.0a0-b0e1c51-vs-3.13.0.svg)

