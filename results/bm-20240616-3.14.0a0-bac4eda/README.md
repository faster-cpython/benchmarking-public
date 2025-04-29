# Results

- fork: python/bac4edad69bb20dd9460
- version: 3.14.0a0
- config: 
- commit hash: [bac4eda](https://github.com/python/cpython/commit/bac4eda)
- commit date: 2024-06-16T22:47:10-07:00
- commit merge base: [bd4516d9efee109dd3b02a3d60845f9053fc6718](https://github.com/python/cpython/commit/bd4516d9efee109dd3b02a3d60845f9053fc6718)
- ref: bac4edad69bb20dd9460

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14715514947)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda.json)

### vs. 3.10.4

- Geometric mean: 1.385x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda-vs-3.10.4.md)
- [📈time plot](bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda-vs-3.12.0.md)
- [📈time plot](bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x slower (HPT: reliability of 99.76%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda-vs-3.13.0.md)
- [📈time plot](bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda-vs-3.13.0.svg)

