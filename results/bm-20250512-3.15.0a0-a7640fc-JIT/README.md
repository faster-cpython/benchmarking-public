# Results

- fork: brandtbucher/justin_compact_exits
- version: 3.15.0a0
- config: JIT
- commit hash: [a7640fc](https://github.com/brandtbucher/cpython/commit/a7640fc)
- commit date: 2025-05-12T19:40:33-07:00
- commit merge base: [121ed71f4e395948d313249b2ad33e1e21581f8a](https://github.com/python/cpython/commit/121ed71f4e395948d313249b2ad33e1e21581f8a)
- ref: justin_compact_exits

## linux x86_64 (azure)

- [pystats raw](bm-20250512-azure-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-pystats.json)
- [pystats table](bm-20250512-azure-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-pystats.md)

### vs. base

- [pystats diff](bm-20250512-azure-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14986971203)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-3.10.4.md)
- [📈time plot](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-3.12.0.md)
- [📈time plot](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x slower (HPT: reliability of 99.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-3.13.0.md)
- [📈time plot](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 65.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-base-mem.svg)
- [📄table](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-base.md)
- [📈time plot](bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc-vs-base.svg)

