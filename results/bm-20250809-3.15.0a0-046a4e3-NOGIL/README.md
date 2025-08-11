# Results

- fork: python/046a4e39b3f8ac5cb13e
- version: 3.15.0a0
- config: NOGIL
- commit hash: [046a4e3](https://github.com/python/cpython/commit/046a4e3)
- commit date: 2025-08-09T18:25:49+00:00
- commit merge base: [af15e1d13ea26575afbb94b814e541586547a706](https://github.com/python/cpython/commit/af15e1d13ea26575afbb94b814e541586547a706)
- ref: 046a4e39b3f8ac5cb13e

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.140x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.67x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x slower (HPT: reliability of 99.73%, 1.01x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x slower (HPT: reliability of 99.92%, 1.01x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.131x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base-mem.svg)
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.66x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x slower (HPT: reliability of 97.70%, 1.00x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x slower (HPT: reliability of 98.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.092x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base-mem.svg)
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.145x faster (HPT: reliability of 99.84%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 98.41%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x slower (HPT: reliability of 99.94%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.126x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.271x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.306x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x faster (HPT: reliability of 97.45%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.123x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 64.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 88.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 98.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base-mem.svg)
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

