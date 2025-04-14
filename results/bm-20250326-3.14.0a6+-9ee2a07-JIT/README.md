# Results

- fork: brandtbucher/jit_up_12_11
- version: 3.14.0a6+
- config: JIT
- commit hash: [9ee2a07](https://github.com/brandtbucher/cpython/commit/9ee2a07)
- commit date: 2025-03-26T11:06:43-07:00
- commit merge base: [a1232459860235f4fb7896cc95966d87a51cbe32](https://github.com/python/cpython/commit/a1232459860235f4fb7896cc95966d87a51cbe32)
- ref: jit_up_12_11

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14090440510)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07.json)

### vs. 3.10.4

- Geometric mean: 1.438x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-3.10.4.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-3.12.0.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 96.80%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-3.13.0.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 78.76%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-base-mem.svg)
- [📄table](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-base.md)
- [📈time plot](bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6%2B-9ee2a07-vs-base.svg)

