# Results

- fork: python/5334732f9c8a44722e4b
- version: 3.15.0a0
- config: 
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

- Geometric mean: 1.129x faster (HPT: reliability of 99.80%, 1.02x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.102x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-arminc-aarch64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250628-azure-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-pystats.json)
- [pystats table](bm-20250628-azure-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.279x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x slower (HPT: reliability of 93.32%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-linux-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.071x slower (HPT: reliability of 99.92%, 1.04x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x slower (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf2-x86_64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.142x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.269x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.273x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.036x slower (HPT: reliability of 99.03%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x slower (HPT: reliability of 79.89%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.126x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-pythonperf1_win32-amd64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15949440274)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732.json)

### vs. 3.10.4

- Geometric mean: 1.245x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x slower (HPT: reliability of 98.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x slower (HPT: reliability of 68.39%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.md)
- [📈time plot](bm-20250628-darwin-arm64-python-5334732f9c8a44722e4b-3.15.0a0-5334732-vs-3.13.0.svg)

