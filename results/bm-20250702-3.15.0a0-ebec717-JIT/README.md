# Results

- fork: brandtbucher/jit_up_6_12
- version: 3.15.0a0
- config: JIT
- commit hash: [ebec717](https://github.com/brandtbucher/cpython/commit/ebec717)
- commit date: 2025-07-02T08:55:39-07:00
- commit merge base: [fa43a1e0f8caf00a15898fa719e31767c866bd90](https://github.com/python/cpython/commit/fa43a1e0f8caf00a15898fa719e31767c866bd90)
- ref: jit_up_6_12

## linux x86_64 (azure)

- [pystats raw](bm-20250702-azure-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-pystats.json)
- [pystats table](bm-20250702-azure-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-pystats.md)

### vs. base

- [pystats diff](bm-20250702-azure-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16035125399)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717.json)

### vs. 3.10.4

- Geometric mean: 1.424x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.10.4.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.12.0.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.13.0.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 80.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-base-mem.svg)
- [📄table](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-base.md)
- [📈time plot](bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717-vs-base.svg)

