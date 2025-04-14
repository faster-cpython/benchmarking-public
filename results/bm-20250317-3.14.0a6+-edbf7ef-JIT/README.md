# Results

- fork: brandtbucher/jit_binary_op_extend
- version: 3.14.0a6+
- config: JIT
- commit hash: [edbf7ef](https://github.com/brandtbucher/cpython/commit/edbf7ef)
- commit date: 2025-03-17T12:07:57-07:00
- commit merge base: [fd545d735d5f9c048f99767c700f72853a9b7acd](https://github.com/python/cpython/commit/fd545d735d5f9c048f99767c700f72853a9b7acd)
- ref: jit_binary_op_extend

## linux x86_64 (azure)

- [pystats raw](bm-20250317-azure-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-pystats.json)
- [pystats table](bm-20250317-azure-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-pystats.md)

### vs. base

- [pystats diff](bm-20250317-azure-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13907848271)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-3.10.4.md)
- [📈time plot](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-3.12.0.md)
- [📈time plot](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 97.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-3.13.0.md)
- [📈time plot](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 55.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-base-mem.svg)
- [📄table](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-base.md)
- [📈time plot](bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6%2B-edbf7ef-vs-base.svg)

