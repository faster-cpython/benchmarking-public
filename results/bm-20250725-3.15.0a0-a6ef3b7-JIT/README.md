# Results

- fork: brandtbucher/jit_shim
- version: 3.15.0a0
- config: JIT
- commit hash: [a6ef3b7](https://github.com/brandtbucher/cpython/commit/a6ef3b7)
- commit date: 2025-07-25T17:26:58-07:00
- commit merge base: [1e69cd1634e4f0f8c375be85d11925bd12deef23](https://github.com/python/cpython/commit/1e69cd1634e4f0f8c375be85d11925bd12deef23)
- ref: jit_shim

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16540876607)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json)

### vs. 3.10.4

- Geometric mean: 1.295x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.md)
- [📈time plot](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 99.82%, 1.01x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.md)
- [📈time plot](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x faster (HPT: reliability of 98.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.md)
- [📈time plot](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 99.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base-mem.svg)
- [📄table](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.md)
- [📈time plot](bm-20250725-arminc-aarch64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16540876607)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json)

### vs. 3.10.4

- Geometric mean: 1.300x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.md)
- [📈time plot](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.md)
- [📈time plot](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 67.67%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.md)
- [📈time plot](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 92.71%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.md)
- [📈time plot](bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16540876607)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json)

### vs. 3.10.4

- Geometric mean: 1.190x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.md)
- [📈time plot](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.md)
- [📈time plot](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x slower (HPT: reliability of 99.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.md)
- [📈time plot](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 97.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base-mem.svg)
- [📄table](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.md)
- [📈time plot](bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7-vs-base.svg)

