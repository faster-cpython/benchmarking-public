# Results

- fork: python/6fcac09401e336b25833
- version: 3.15.0a0
- config: 
- commit hash: [6fcac09](https://github.com/python/cpython/commit/6fcac09)
- commit date: 2025-08-23T15:18:46+00:00
- commit merge base: [ab1bef8ad27ad531a1109cfc016ea627d94f9cc1](https://github.com/python/cpython/commit/ab1bef8ad27ad531a1109cfc016ea627d94f9cc1)
- ref: 6fcac09401e336b25833

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.334x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.069x faster (HPT: reliability of 74.27%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.465x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.483x faster (HPT: reliability of 100.00%, 1.44x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.282x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: missing
- platform: macOS-15.6-arm64-arm-64bit-Mach-O
- [raw results](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.324x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 89.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

