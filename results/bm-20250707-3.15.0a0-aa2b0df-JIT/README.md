# Results

- fork: brandtbucher/jit_targets
- version: 3.15.0a0
- config: JIT
- commit hash: [aa2b0df](https://github.com/brandtbucher/cpython/commit/aa2b0df)
- commit date: 2025-07-07T15:40:19-07:00
- commit merge base: [0240ef4705d835e27beb2437dfadb5d34aa2db17](https://github.com/python/cpython/commit/0240ef4705d835e27beb2437dfadb5d34aa2db17)
- ref: jit_targets

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16131305975)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json)

### vs. 3.10.4

- Geometric mean: 1.220x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.10.4.md)
- [📈time plot](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x slower (HPT: reliability of 51.56%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.12.0.md)
- [📈time plot](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x slower (HPT: reliability of 60.77%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.13.0.md)
- [📈time plot](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.044x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base-mem.svg)
- [📄table](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base.md)
- [📈time plot](bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250707-azure-x86_64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-pystats.json)
- [pystats table](bm-20250707-azure-x86_64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-pystats.md)

### vs. base

- [pystats diff](bm-20250707-azure-x86_64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-pystats-vs-base.md)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16131305975)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.10.4.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.12.0.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.086x faster (HPT: reliability of 89.45%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.13.0.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 89.28%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base.md)
- [📈time plot](bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16131305975)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json)

### vs. 3.10.4

- Geometric mean: 1.342x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.10.4.md)
- [📈time plot](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 95.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.12.0.md)
- [📈time plot](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.13.0.md)
- [📈time plot](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 89.49%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base-mem.svg)
- [📄table](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base.md)
- [📈time plot](bm-20250707-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-aa2b0df-vs-base.svg)

