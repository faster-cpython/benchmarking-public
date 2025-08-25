# Results

- fork: python/6fcac09401e336b25833
- version: 3.15.0a0
- config: NOGIL
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

- Geometric mean: 1.132x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.68x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.093x slower (HPT: reliability of 99.80%, 1.02x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x slower (HPT: reliability of 99.95%, 1.01x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.135x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base-mem.svg)
- [📄table](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.md)
- [📈time plot](bm-20250823-arminc-aarch64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.65x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.056x slower (HPT: reliability of 97.49%, 1.00x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x slower (HPT: reliability of 95.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.095x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base-mem.svg)
- [📄table](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.md)
- [📈time plot](bm-20250823-pythonperf2-x86_64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.162x faster (HPT: reliability of 99.96%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.005x faster (HPT: reliability of 97.58%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.054x slower (HPT: reliability of 99.91%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.115x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.md)
- [📈time plot](bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.339x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.135x faster (HPT: reliability of 99.67%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.116x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.md)
- [📈time plot](bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17181621677)
- cpu model: missing
- platform: macOS-15.6-arm64-arm-64bit-Mach-O
- [raw results](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json)

### vs. 3.10.4

- Geometric mean: 1.279x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.md)
- [📈time plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x faster (HPT: reliability of 55.52%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.md)
- [📈time plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 84.34%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.md)
- [📈time plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.020x slower (HPT: reliability of 98.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base-mem.svg)
- [📄table](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.md)
- [📈time plot](bm-20250823-darwin-arm64-python-6fcac09401e336b25833-3.15.0a0-6fcac09-vs-base.svg)

