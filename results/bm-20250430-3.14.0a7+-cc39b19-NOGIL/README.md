# Results

- fork: python/cc39b19f0fca8db0f881
- version: 3.14.0a7+
- config: NOGIL
- commit hash: [cc39b19](https://github.com/python/cpython/commit/cc39b19)
- commit date: 2025-04-30T16:41:50+03:00
- commit merge base: [8b26b23a9674a02563f28e4cfbef3d3e39876bfe](https://github.com/python/cpython/commit/8b26b23a9674a02563f28e4cfbef3d3e39876bfe)
- ref: cc39b19f0fca8db0f881

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14757480119)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19.json)

### vs. 3.10.4

- Geometric mean: 1.312x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-3.10.4.md)
- [📈time plot](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x faster (HPT: reliability of 83.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-3.12.0.md)
- [📈time plot](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 99.94%, 1.02x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-3.13.0.md)
- [📈time plot](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.072x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.18x
- [🧠memory plot](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-base-mem.svg)
- [📄table](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-base.md)
- [📈time plot](bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7%2B-cc39b19-vs-base.svg)

