# Results

- fork: brandtbucher/justin_hot
- version: 3.15.0a0
- config: JIT
- commit hash: [858624a](https://github.com/brandtbucher/cpython/commit/858624a)
- commit date: 2025-06-12T13:37:31-07:00
- commit merge base: [0f866cbfefd797b4dae25962457c5579bb90dde5](https://github.com/python/cpython/commit/0f866cbfefd797b4dae25962457c5579bb90dde5)
- ref: justin_hot

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15621148816)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a.json)

### vs. 3.10.4

- Geometric mean: 1.149x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.10.4.md)
- [📈time plot](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x slower (HPT: reliability of 54.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.12.0.md)
- [📈time plot](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x slower (HPT: reliability of 70.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.13.0.md)
- [📈time plot](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.040x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-base-mem.svg)
- [📄table](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-base.md)
- [📈time plot](bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250612-azure-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-pystats.json)
- [pystats table](bm-20250612-azure-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-pystats.md)

### vs. base

- [pystats diff](bm-20250612-azure-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15621137551)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a.json)

### vs. 3.10.4

- Geometric mean: 1.337x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.10.4.md)
- [📈time plot](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.12.0.md)
- [📈time plot](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x slower (HPT: reliability of 99.31%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.13.0.md)
- [📈time plot](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-base-mem.svg)
- [📄table](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-base.md)
- [📈time plot](bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a-vs-base.svg)

