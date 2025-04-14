# Results

- fork: brandtbucher/keep_stack_pointer
- version: 3.14.0a6+
- config: 
- commit hash: [b3d84fd](https://github.com/brandtbucher/cpython/commit/b3d84fd)
- commit date: 2025-03-26T14:29:09-07:00
- commit merge base: [4b3d5b604210f68005ef64d5346ca169385f5acf](https://github.com/python/cpython/commit/4b3d5b604210f68005ef64d5346ca169385f5acf)
- ref: keep_stack_pointer

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14121931128)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd.json)

### vs. 3.10.4

- Geometric mean: 1.494x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.10.4.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.152x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.12.0.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.13.0.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-base-mem.svg)
- [📄table](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-base.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6%2B-b3d84fd-vs-base.svg)

