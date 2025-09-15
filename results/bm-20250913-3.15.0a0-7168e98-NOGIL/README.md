# Results

- fork: python/7168e98c80d28ab71f39
- version: 3.15.0a0
- config: NOGIL
- commit hash: [7168e98](https://github.com/python/cpython/commit/7168e98)
- commit date: 2025-09-13T19:27:04+02:00
- commit merge base: [430900d15b3d3abb5c6460fbdbf90f4d6561397d](https://github.com/python/cpython/commit/430900d15b3d3abb5c6460fbdbf90f4d6561397d)
- ref: 7168e98c80d28ab71f39

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17703689261)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json)

### vs. 3.10.4

- Geometric mean: 1.208x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.66x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.10.4.md)
- [📈time plot](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x slower (HPT: reliability of 95.55%, 1.00x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.12.0.md)
- [📈time plot](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x slower (HPT: reliability of 93.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.13.0.md)
- [📈time plot](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-base-mem.svg)
- [📄table](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-base.md)
- [📈time plot](bm-20250913-pythonperf2-x86_64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17703689261)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json)

### vs. 3.10.4

- Geometric mean: 1.145x faster (HPT: reliability of 99.85%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.10.4.md)
- [📈time plot](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 98.57%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.12.0.md)
- [📈time plot](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x slower (HPT: reliability of 99.97%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.13.0.md)
- [📈time plot](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.132x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-base.md)
- [📈time plot](bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17703689261)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json)

### vs. 3.10.4

- Geometric mean: 1.291x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.10.4.md)
- [📈time plot](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.324x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.12.0.md)
- [📈time plot](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.119x faster (HPT: reliability of 99.03%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.13.0.md)
- [📈time plot](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.122x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-base.md)
- [📈time plot](bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98-vs-base.svg)

