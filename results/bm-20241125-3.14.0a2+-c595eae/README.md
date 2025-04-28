# Results

- fork: python/c595eae84c7f665eced0
- version: 3.14.0a2+
- config: 
- commit hash: [c595eae](https://github.com/python/cpython/commit/c595eae)
- commit date: 2024-11-25T00:29:55-05:00
- commit merge base: [17c16aea66b606d66f71ae9af381bc34d0ef3f5f](https://github.com/python/cpython/commit/17c16aea66b606d66f71ae9af381bc34d0ef3f5f)
- ref: c595eae84c7f665eced0

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673983832)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae.json)

### vs. 3.10.4

- Geometric mean: 1.386x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.10.4.md)
- [📈time plot](bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.12.0.md)
- [📈time plot](bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 76.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.13.0.md)
- [📈time plot](bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2%2B-c595eae-vs-3.13.0.svg)

