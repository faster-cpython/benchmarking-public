# Results

- fork: brandtbucher/justin_hot
- version: 3.15.0a0
- config: JIT
- commit hash: [5606078](https://github.com/brandtbucher/cpython/commit/5606078)
- commit date: 2025-06-11T18:48:45-07:00
- commit merge base: [0f866cbfefd797b4dae25962457c5579bb90dde5](https://github.com/python/cpython/commit/0f866cbfefd797b4dae25962457c5579bb90dde5)
- ref: justin_hot

## linux x86_64 (azure)

- [pystats raw](bm-20250611-azure-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-pystats.json)
- [pystats table](bm-20250611-azure-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-pystats.md)

### vs. base

- [pystats diff](bm-20250611-azure-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15599692843)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078.json)

### vs. 3.10.4

- Geometric mean: 1.342x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-3.10.4.md)
- [📈time plot](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-3.12.0.md)
- [📈time plot](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x slower (HPT: reliability of 99.60%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-3.13.0.md)
- [📈time plot](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-base-mem.svg)
- [📄table](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-base.md)
- [📈time plot](bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078-vs-base.svg)

