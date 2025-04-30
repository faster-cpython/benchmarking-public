# Results

- fork: kumaraditya303/experiment_gc_async
- version: 3.14.0a7+
- config: 
- commit hash: [bd38cdb](https://github.com/kumaraditya303/cpython/commit/bd38cdb)
- commit date: 2025-04-30T19:58:17+05:30
- commit merge base: [cc39b19f0fca8db0f881ecaf02f88d72d9f93776](https://github.com/python/cpython/commit/cc39b19f0fca8db0f881ecaf02f88d72d9f93776)
- ref: experiment_gc_async

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14757475809)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7%2B-bd38cdb.json)

### vs. 3.10.4

- Geometric mean: 1.423x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7%2B-bd38cdb-vs-3.10.4.md)
- [📈time plot](bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7%2B-bd38cdb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7%2B-bd38cdb-vs-3.12.0.md)
- [📈time plot](bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7%2B-bd38cdb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x faster (HPT: reliability of 87.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7%2B-bd38cdb-vs-3.13.0.md)
- [📈time plot](bm-20250430-linux-x86_64-kumaraditya303-experiment_gc_async-3.14.0a7%2B-bd38cdb-vs-3.13.0.svg)

