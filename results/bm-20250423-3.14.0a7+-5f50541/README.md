# Results

- fork: python/5f50541ebd420a2d21a2
- version: 3.14.0a7+
- config: 
- commit hash: [5f50541](https://github.com/python/cpython/commit/5f50541)
- commit date: 2025-04-23T14:27:21+03:00
- commit merge base: [d7be26a71e74818c4df60f31c879e52da2e1e94e](https://github.com/python/cpython/commit/d7be26a71e74818c4df60f31c879e52da2e1e94e)
- ref: 5f50541ebd420a2d21a2

## linux x86_64 (azure)

- [pystats raw](bm-20250423-azure-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-pystats.json)
- [pystats table](bm-20250423-azure-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14718617209)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-vs-3.10.4.md)
- [📈time plot](bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.122x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-vs-3.12.0.md)
- [📈time plot](bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-vs-3.13.0.md)
- [📈time plot](bm-20250423-linux-x86_64-python-5f50541ebd420a2d21a2-3.14.0a7%2B-5f50541-vs-3.13.0.svg)

