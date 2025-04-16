# Results

- fork: mdboom/fast_tuple_dealloc
- version: 3.14.0a7+
- config: 
- commit hash: [661a2b8](https://github.com/mdboom/cpython/commit/661a2b8)
- commit date: 2025-04-15T18:28:35-04:00
- commit merge base: [2ff5eb8582939eb9182d3449d08542881caf3e0d](https://github.com/python/cpython/commit/2ff5eb8582939eb9182d3449d08542881caf3e0d)
- ref: fast_tuple_dealloc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14480596125)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8.json)

### vs. 3.10.4

- Geometric mean: 1.445x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-3.10.4.md)
- [📈time plot](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-3.12.0.md)
- [📈time plot](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-3.13.0.md)
- [📈time plot](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-base-mem.svg)
- [📄table](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-base.md)
- [📈time plot](bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7%2B-661a2b8-vs-base.svg)

