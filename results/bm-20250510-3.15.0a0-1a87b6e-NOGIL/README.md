# Results

- fork: python/1a87b6e9ae6da255f304
- version: 3.15.0a0
- config: NOGIL
- commit hash: [1a87b6e](https://github.com/python/cpython/commit/1a87b6e)
- commit date: 2025-05-10T22:37:17+00:00
- commit merge base: [dc191d248456855d228b09f0e0206e0b656f113c](https://github.com/python/cpython/commit/dc191d248456855d228b09f0e0206e0b656f113c)
- ref: 1a87b6e9ae6da255f304

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- Geometric mean: 1.174x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.64x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x slower (HPT: reliability of 99.85%, 1.02x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x slower (HPT: reliability of 99.93%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.054x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.22x
- [🧠memory plot](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.58x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 73.31%, 1.00x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x slower (HPT: reliability of 99.83%, 1.01x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- Geometric mean: 1.239x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.61x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x slower (HPT: reliability of 99.87%, 1.02x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 97.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- Geometric mean: 1.166x faster (HPT: reliability of 99.94%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.005x faster (HPT: reliability of 94.90%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x slower (HPT: reliability of 99.95%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- Geometric mean: 1.013x faster (HPT: reliability of 58.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 98.20%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.101x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.123x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14950305273)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json)

### vs. 3.10.4

- Geometric mean: 1.189x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.md)
- [📈time plot](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x slower (HPT: reliability of 99.49%, 1.00x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.md)
- [📈time plot](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x slower (HPT: reliability of 99.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.md)
- [📈time plot](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.056x faster (HPT: reliability of 91.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base-mem.svg)
- [📄table](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.md)
- [📈time plot](bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e-vs-base.svg)

