# Results

- fork: python/5334732f9c8a44722e4b
- version: 3.15.0a0
- config: NOGIL
- commit hash: [5334732](https://github.com/python/cpython/commit/5334732)
- commit date: 2025-06-28T14:11:31+01:00
- commit merge base: [579acf45629fa0b7787ec78fa4049fc6a6388b71](https://github.com/python/cpython/commit/579acf45629fa0b7787ec78fa4049fc6a6388b71)
- ref: 5334732f9c8a44722e4b

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.056x slower (HPT: reliability of 97.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.68x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.244x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.245x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.162x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.104x faster (HPT: reliability of 99.31%, 1.00x faster at 99th %ile)
- Memory usage: 1.57x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x slower (HPT: reliability of 99.98%, 1.05x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.191x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.125x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.049x faster (HPT: reliability of 89.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.67x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.173x slower (HPT: reliability of 99.99%, 1.10x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.165x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.114x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.310x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.405x slower (HPT: reliability of 100.00%, 1.55x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.418x slower (HPT: reliability of 100.00%, 1.67x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.200x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.225x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.206x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.302x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.201x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.170x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x slower (HPT: reliability of 99.86%, 1.02x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x slower (HPT: reliability of 99.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.048x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base-mem.svg)
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-base.svg)

