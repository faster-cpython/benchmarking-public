# Results

- fork: brandtbucher/jit_oz
- version: 3.15.0a0
- config: JIT
- commit hash: [6448067](https://github.com/brandtbucher/cpython/commit/6448067)
- commit date: 2025-06-28T10:16:47-07:00
- commit merge base: [c419af9e277bea7dd78f4defefc752fe93b0b8ec](https://github.com/python/cpython/commit/c419af9e277bea7dd78f4defefc752fe93b0b8ec)
- ref: jit_oz

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16177380102)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067.json)

### vs. 3.10.4

- Geometric mean: 1.308x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.md)
- [📈time plot](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 88.63%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 88.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base-mem.svg)
- [📄table](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)
- [📈time plot](bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250628-azure-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-pystats.json)
- [pystats table](bm-20250628-azure-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-pystats.md)

### vs. base

- [pystats diff](bm-20250628-azure-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16177380102)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067.json)

### vs. 3.10.4

- Geometric mean: 1.356x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base-mem.svg)
- [📄table](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)

## linux x86_64 (pythonperf2_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16177380102)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067.json)

### vs. base

- Geometric mean: 1.015x slower (HPT: reliability of 99.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base-mem.svg)
- [📄table](bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)
- [📈time plot](bm-20250628-pythonperf2_clang-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16177380102)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.083x faster (HPT: reliability of 81.42%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 88.90%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16177380102)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16177380102)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json)

### vs. 3.10.4

- Geometric mean: 1.472x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.494x faster (HPT: reliability of 100.00%, 1.44x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.300x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 77.59%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)

## windows amd64 (pythonperf1_win32_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16177380102)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 99.78%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1_win32_clang-amd64-brandtbucher-jit_oz-3.15.0a0-6448067-vs-base.svg)

