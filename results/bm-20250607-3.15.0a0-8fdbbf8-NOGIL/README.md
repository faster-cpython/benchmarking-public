# Results

- fork: python/8fdbbf8b18f1405abe67
- version: 3.15.0a0
- config: NOGIL
- commit hash: [8fdbbf8](https://github.com/python/cpython/commit/8fdbbf8)
- commit date: 2025-06-07T14:08:44-07:00
- commit merge base: [ac9c3431cc5916a795c42b3e2b965233ceffe6f0](https://github.com/python/cpython/commit/ac9c3431cc5916a795c42b3e2b965233ceffe6f0)
- ref: 8fdbbf8b18f1405abe67

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15512862488)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json)

### vs. 3.10.4

- Geometric mean: 1.078x slower (HPT: reliability of 98.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.71x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.md)
- [📈time plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.265x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.md)
- [📈time plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.264x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.md)
- [📈time plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.050x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.23x
- [🧠memory plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base-mem.svg)
- [📄table](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.md)
- [📈time plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15512862488)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json)

### vs. 3.10.4

- Geometric mean: 1.074x faster (HPT: reliability of 98.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.59x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.155x slower (HPT: reliability of 99.98%, 1.07x slower at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.208x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.059x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.22x
- [🧠memory plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base-mem.svg)
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15512862488)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json)

### vs. 3.10.4

- Geometric mean: 1.011x faster (HPT: reliability of 84.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.67x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.md)
- [📈time plot](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.204x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.md)
- [📈time plot](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.191x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.md)
- [📈time plot](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.091x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base-mem.svg)
- [📄table](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.md)
- [📈time plot](bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15512862488)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json)

### vs. 3.10.4

- Geometric mean: 1.155x faster (HPT: reliability of 98.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.md)
- [📈time plot](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x slower (HPT: reliability of 99.89%, 1.02x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.md)
- [📈time plot](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.068x slower (HPT: reliability of 99.74%, 1.00x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.md)
- [📈time plot](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x faster (HPT: reliability of 99.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base-mem.svg)
- [📄table](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.md)
- [📈time plot](bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.svg)

