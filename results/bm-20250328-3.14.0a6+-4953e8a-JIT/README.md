# Results

- fork: brandtbucher/jit_cached_consts
- version: 3.14.0a6+
- config: JIT
- commit hash: [4953e8a](https://github.com/brandtbucher/cpython/commit/4953e8a)
- commit date: 2025-03-28T16:47:23-07:00
- commit merge base: [fd545d735d5f9c048f99767c700f72853a9b7acd](https://github.com/python/cpython/commit/fd545d735d5f9c048f99767c700f72853a9b7acd)
- ref: jit_cached_consts

## linux x86_64 (azure)

- [pystats raw](bm-20250328-azure-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-pystats.json)
- [pystats table](bm-20250328-azure-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-pystats.md)

### vs. base

- [pystats diff](bm-20250328-azure-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14140004429)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a.json)

### vs. 3.10.4

- Geometric mean: 1.453x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-3.10.4.md)
- [📈time plot](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-3.12.0.md)
- [📈time plot](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.83%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-3.13.0.md)
- [📈time plot](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-base-mem.svg)
- [📄table](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-base.md)
- [📈time plot](bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6%2B-4953e8a-vs-base.svg)

