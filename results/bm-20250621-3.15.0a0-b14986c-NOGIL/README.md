# Results

- fork: python/b14986c91464b06e9016
- version: 3.15.0a0
- config: NOGIL
- commit hash: [b14986c](https://github.com/python/cpython/commit/b14986c)
- commit date: 2025-06-21T22:03:17+05:30
- commit merge base: [6a16b3c440cf9ecabecd3e90f44310e3b0765780](https://github.com/python/cpython/commit/6a16b3c440cf9ecabecd3e90f44310e3b0765780)
- ref: b14986c91464b06e9016

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.076x slower (HPT: reliability of 96.33%, 1.00x slower at 99th %ile)
- Memory usage: 1.72x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.263x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.262x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.078x faster (HPT: reliability of 98.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.59x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.152x slower (HPT: reliability of 99.98%, 1.07x slower at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.205x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.015x faster (HPT: reliability of 87.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.69x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.201x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.188x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.313x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.406x slower (HPT: reliability of 100.00%, 1.54x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.417x slower (HPT: reliability of 100.00%, 1.65x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.228x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.209x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.301x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.162x faster (HPT: reliability of 99.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x slower (HPT: reliability of 99.87%, 1.02x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x slower (HPT: reliability of 99.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

