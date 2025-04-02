# Results

- fork: brandtbucher/jit_guard_dict_tuple
- version: 3.14.0a6+
- config: JIT
- commit hash: [99d6288](https://github.com/brandtbucher/cpython/commit/99d6288)
- commit date: 2025-04-01T18:05:30-07:00
- commit merge base: [1a9d4a1fb3d4beda7c7e8483af7c6bc7ac477e9f](https://github.com/python/cpython/commit/1a9d4a1fb3d4beda7c7e8483af7c6bc7ac477e9f)
- ref: jit_guard_dict_tuple

## linux x86_64 (azure)

- [pystats raw](bm-20250401-azure-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-pystats.json)
- [pystats table](bm-20250401-azure-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-pystats.md)

### vs. base

- [pystats diff](bm-20250401-azure-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14209259473)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288.json)

### vs. 3.10.4

- Geometric mean: 1.472x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-3.10.4.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.136x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-3.12.0.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-3.13.0.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 54.10%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-base-mem.svg)
- [📄table](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-base.md)
- [📈time plot](bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6%2B-99d6288-vs-base.svg)

