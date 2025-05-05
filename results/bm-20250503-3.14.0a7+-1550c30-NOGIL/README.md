# Results

- fork: python/1550c30fd5f2f2902bbc
- version: 3.14.0a7+
- config: NOGIL
- commit hash: [1550c30](https://github.com/python/cpython/commit/1550c30)
- commit date: 2025-05-03T15:05:04+03:00
- commit merge base: [77c391a1b178a35b0157e00689acb3904b77694d](https://github.com/python/cpython/commit/77c391a1b178a35b0157e00689acb3904b77694d)
- ref: 1550c30fd5f2f2902bbc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14837701367)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30.json)

### vs. 3.10.4

- Geometric mean: 1.307x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-3.10.4.md)
- [📈time plot](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x faster (HPT: reliability of 88.31%, 1.00x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-3.12.0.md)
- [📈time plot](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x slower (HPT: reliability of 99.86%, 1.02x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-3.13.0.md)
- [📈time plot](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.082x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.18x
- [🧠memory plot](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-base-mem.svg)
- [📄table](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-base.md)
- [📈time plot](bm-20250503-linux-x86_64-python-1550c30fd5f2f2902bbc-3.14.0a7%2B-1550c30-vs-base.svg)

