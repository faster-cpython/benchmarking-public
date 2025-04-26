# Results

- fork: python/25441592db179e9f5e6c
- version: 3.14.0a1+
- config: 
- commit hash: [2544159](https://github.com/python/cpython/commit/2544159)
- commit date: 2024-10-28T10:30:31+00:00
- commit merge base: [19e93e2e269889ecb3c4c039091abff489f247c2](https://github.com/python/cpython/commit/19e93e2e269889ecb3c4c039091abff489f247c2)
- ref: 25441592db179e9f5e6c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673983033)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159.json)

### vs. 3.10.4

- Geometric mean: 1.394x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.10.4.md)
- [📈time plot](bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.12.0.md)
- [📈time plot](bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.000x faster (HPT: reliability of 59.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.13.0.md)
- [📈time plot](bm-20241028-linux-x86_64-python-25441592db179e9f5e6c-3.14.0a1%2B-2544159-vs-3.13.0.svg)

