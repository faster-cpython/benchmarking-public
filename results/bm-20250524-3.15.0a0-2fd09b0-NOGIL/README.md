# Results

- fork: python/2fd09b011031f3c00c34
- version: 3.15.0a0
- config: NOGIL
- commit hash: [2fd09b0](https://github.com/python/cpython/commit/2fd09b0)
- commit date: 2025-05-24T12:19:20+00:00
- commit merge base: [5d9c8fe3f6168785cb608dddd3010042f39bb226](https://github.com/python/cpython/commit/5d9c8fe3f6168785cb608dddd3010042f39bb226)
- ref: 2fd09b011031f3c00c34

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15232174341)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json)

### vs. 3.10.4

- Geometric mean: 1.170x faster (HPT: reliability of 99.99%, 1.06x faster at 99th %ile)
- Memory usage: 1.65x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x slower (HPT: reliability of 99.80%, 1.01x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x slower (HPT: reliability of 99.89%, 1.01x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)
- [📈time plot](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base-mem.svg)
- [📄table](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.md)
- [📈time plot](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15232174341)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json)

### vs. 3.10.4

- Geometric mean: 1.298x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.58x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 80.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x slower (HPT: reliability of 99.86%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)
- [📈time plot](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base-mem.svg)
- [📄table](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.md)
- [📈time plot](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15232174341)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json)

### vs. 3.10.4

- Geometric mean: 1.237x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.61x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x slower (HPT: reliability of 99.68%, 1.01x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x slower (HPT: reliability of 95.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)
- [📈time plot](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base-mem.svg)
- [📄table](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.md)
- [📈time plot](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15232174341)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json)

### vs. 3.10.4

- Geometric mean: 1.147x faster (HPT: reliability of 99.67%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x slower (HPT: reliability of 97.27%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x slower (HPT: reliability of 99.96%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)
- [📈time plot](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.md)
- [📈time plot](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15232174341)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json)

### vs. 3.10.4

- Geometric mean: 1.052x faster (HPT: reliability of 71.69%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 99.94%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x slower (HPT: reliability of 99.98%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)
- [📈time plot](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.md)
- [📈time plot](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15232174341)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json)

### vs. 3.10.4

- Geometric mean: 1.188x faster (HPT: reliability of 99.98%, 1.04x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x slower (HPT: reliability of 99.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x slower (HPT: reliability of 99.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base-mem.svg)
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.svg)

