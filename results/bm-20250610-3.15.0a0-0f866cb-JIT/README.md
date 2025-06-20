# Results

- fork: python/main
- version: 3.15.0a0
- config: JIT
- commit hash: [0f866cb](https://github.com/python/cpython/commit/0f866cb)
- commit date: 2025-06-10T13:38:32+00:00
- commit merge base: [ff2b5f40c2bf5c71255caac8a743c09ba0758c02](https://github.com/python/cpython/commit/ff2b5f40c2bf5c71255caac8a743c09ba0758c02)
- fork: python/0f866cbfefd797b4dae2
- ref: 0f866cbfefd797b4dae2, main

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15565651398)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15770125023)
- [raw results](bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json)
- [raw results](bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb.json)

### vs. 3.10.4

- Geometric mean: 1.203x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- Geometric mean: 1.325x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.39x
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.svg)
- [📄table](bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x slower (HPT: reliability of 97.10%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- Geometric mean: 1.046x faster (HPT: reliability of 99.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.svg)
- [📄table](bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 94.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- Geometric mean: 1.044x faster (HPT: reliability of 98.57%, 1.00x faster at 99th %ile)
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- [📄table](bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-arminc-aarch64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.svg)
- [📄table](bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250610-azure-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-pystats.json)
- [pystats table](bm-20250610-azure-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15565651398)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15770125023)
- [raw results](bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json)
- [raw results](bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb.json)

### vs. 3.10.4

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- Geometric mean: 1.465x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.svg)
- [📄table](bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- Geometric mean: 1.127x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.svg)
- [📄table](bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 94.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- Geometric mean: 1.052x faster (HPT: reliability of 98.98%, 1.00x faster at 99th %ile)
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- [📄table](bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.svg)
- [📄table](bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15565651398)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15770125023)
- [raw results](bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json)
- [raw results](bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb.json)

### vs. 3.10.4

- Geometric mean: 1.183x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- Geometric mean: 1.302x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- [📄table](bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.svg)
- [📄table](bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- [📄table](bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.svg)
- [📄table](bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 54.54%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- Geometric mean: 1.078x faster (HPT: reliability of 64.84%, 1.00x faster at 99th %ile)
- [📄table](bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.svg)
- [📄table](bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-pythonperf1-amd64-python-main-3.15.0a0-0f866cb-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15565651398)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15770125023)
- [raw results](bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json)
- [raw results](bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb.json)

### vs. 3.10.4

- Geometric mean: 1.169x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- Geometric mean: 1.262x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- [📄table](bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.10.4.svg)
- [📄table](bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb-vs-3.10.4.md)
- [📈time plot](bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.071x slower (HPT: reliability of 96.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- Geometric mean: 1.004x slower (HPT: reliability of 90.74%, 1.00x slower at 99th %ile)
- [📄table](bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.12.0.svg)
- [📄table](bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb-vs-3.12.0.md)
- [📈time plot](bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.069x slower (HPT: reliability of 61.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- Geometric mean: 1.002x slower (HPT: reliability of 50.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- [📄table](bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb-vs-3.13.0.svg)
- [📄table](bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb-vs-3.13.0.md)
- [📈time plot](bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb-vs-3.13.0.svg)

