# Results

- fork: python/e0bc9d2a0c448cf46df2
- version: 3.14.0a5+
- config: JIT
- commit hash: [e0bc9d2](https://github.com/python/cpython/commit/e0bc9d2)
- commit date: 2025-03-11T12:45:31-04:00
- commit merge base: [9d759b63d8028a987ffad4e8750b13ecfa934967](https://github.com/python/cpython/commit/9d759b63d8028a987ffad4e8750b13ecfa934967)
- ref: e0bc9d2a0c448cf46df2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13864750757)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2.json)

### vs. 3.10.4

- Geometric mean: 1.450x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.10.4.md)
- [📈time plot](bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.12.0.md)
- [📈time plot](bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 99.66%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.13.0.md)
- [📈time plot](bm-20250311-linux-x86_64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13842614400)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2.json)

### vs. 3.10.4

- Geometric mean: 1.279x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.10.4.md)
- [📈time plot](bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.008x faster (HPT: reliability of 86.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.12.0.md)
- [📈time plot](bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x faster (HPT: reliability of 85.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.13.0.md)
- [📈time plot](bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5%2B-e0bc9d2-vs-3.13.0.svg)

