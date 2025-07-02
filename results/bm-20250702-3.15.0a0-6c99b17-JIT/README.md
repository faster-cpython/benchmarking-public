# Results

- fork: brandtbucher/jit_up_6_6
- version: 3.15.0a0
- config: JIT
- commit hash: [6c99b17](https://github.com/brandtbucher/cpython/commit/6c99b17)
- commit date: 2025-07-02T08:55:19-07:00
- commit merge base: [fa43a1e0f8caf00a15898fa719e31767c866bd90](https://github.com/python/cpython/commit/fa43a1e0f8caf00a15898fa719e31767c866bd90)
- ref: jit_up_6_6

## linux x86_64 (azure)

- [pystats raw](bm-20250702-azure-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-pystats.json)
- [pystats table](bm-20250702-azure-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-pystats.md)

### vs. base

- [pystats diff](bm-20250702-azure-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16029957502)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17.json)

### vs. 3.10.4

- Geometric mean: 1.421x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.10.4.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.12.0.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 99.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.13.0.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 61.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-base-mem.svg)
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-base.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17-vs-base.svg)

