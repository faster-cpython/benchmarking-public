# Results

- fork: brandtbucher/jit_targets
- version: 3.15.0a0
- config: JIT
- commit hash: [997a858](https://github.com/brandtbucher/cpython/commit/997a858)
- commit date: 2025-07-08T17:21:50-07:00
- commit merge base: [0240ef4705d835e27beb2437dfadb5d34aa2db17](https://github.com/python/cpython/commit/0240ef4705d835e27beb2437dfadb5d34aa2db17)
- ref: jit_targets

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. 3.10.4

- Geometric mean: 1.286x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.md)
- [📈time plot](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 99.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.md)
- [📈time plot](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x faster (HPT: reliability of 97.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.md)
- [📈time plot](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base-mem.svg)
- [📄table](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250708-azure-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-pystats.json)
- [pystats table](bm-20250708-azure-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-pystats.md)

### vs. base

- [pystats diff](bm-20250708-azure-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. 3.10.4

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 94.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base-mem.svg)
- [📄table](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

## linux x86_64 (pythonperf2_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 99.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base-mem.svg)
- [📄table](bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-pythonperf2_clang-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. 3.10.4

- Geometric mean: 1.317x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.090x faster (HPT: reliability of 90.51%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 94.47%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 98.82%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-pythonperf1_clang-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. 3.10.4

- Geometric mean: 1.476x faster (HPT: reliability of 100.00%, 1.37x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.md)
- [📈time plot](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.497x faster (HPT: reliability of 100.00%, 1.44x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.md)
- [📈time plot](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.md)
- [📈time plot](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 93.96%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. 3.10.4

- Geometric mean: 1.365x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.md)
- [📈time plot](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.076x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.md)
- [📈time plot](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.md)
- [📈time plot](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base-mem.svg)
- [📄table](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16157891710)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858.json)

### vs. base

- Geometric mean: 1.017x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base-mem.svg)
- [📄table](bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.md)
- [📈time plot](bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858-vs-base.svg)

