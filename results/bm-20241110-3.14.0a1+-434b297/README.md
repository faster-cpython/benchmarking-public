# Results

- fork: python/434b29767f2fdef9f35c
- version: 3.14.0a1+
- config: 
- commit hash: [434b297](https://github.com/python/cpython/commit/434b297)
- commit date: 2024-11-10T16:40:25-08:00
- commit merge base: [f435de6765e0327995850d719534be38c9b5ec49](https://github.com/python/cpython/commit/f435de6765e0327995850d719534be38c9b5ec49)
- ref: 434b29767f2fdef9f35c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673983486)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297.json)

### vs. 3.10.4

- Geometric mean: 1.376x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.10.4.md)
- [📈time plot](bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.048x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.12.0.md)
- [📈time plot](bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 98.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.13.0.md)
- [📈time plot](bm-20241110-linux-x86_64-python-434b29767f2fdef9f35c-3.14.0a1%2B-434b297-vs-3.13.0.svg)

