# Results

- fork: python/0ae8579b85f9b0cd3f28
- version: 3.14.0a0
- config: 
- commit hash: [0ae8579](https://github.com/python/cpython/commit/0ae8579)
- commit date: 2024-06-09T22:23:30-04:00
- commit merge base: [34f5ae69fe9ab0f5b23311d5c396d0cbb5902913](https://github.com/python/cpython/commit/34f5ae69fe9ab0f5b23311d5c396d0cbb5902913)
- ref: 0ae8579b85f9b0cd3f28

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14715514762)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579.json)

### vs. 3.10.4

- Geometric mean: 1.395x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.10.4.md)
- [📈time plot](bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.12.0.md)
- [📈time plot](bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x slower (HPT: reliability of 86.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.13.0.md)
- [📈time plot](bm-20240609-linux-x86_64-python-0ae8579b85f9b0cd3f28-3.14.0a0-0ae8579-vs-3.13.0.svg)

