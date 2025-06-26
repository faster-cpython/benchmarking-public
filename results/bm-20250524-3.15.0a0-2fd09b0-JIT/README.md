# Results

- fork: python/2fd09b011031f3c00c34
- version: 3.15.0a0
- config: JIT
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

- Geometric mean: 1.193x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x slower (HPT: reliability of 97.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-arminc-aarch64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x slower (HPT: reliability of 85.80%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
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

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.083x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-linux-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x slower (HPT: reliability of 97.79%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
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

- Geometric mean: 1.348x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, djangocms, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x faster (HPT: reliability of 93.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, djangocms, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-pythonperf2-x86_64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.01%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
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

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 67.67%, 1.00x faster at 99th %ile)
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

- Geometric mean: 1.096x faster (HPT: reliability of 99.72%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-pythonperf1_win32-x86-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x slower (HPT: reliability of 99.98%, 1.03x slower at 99th %ile)
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

- Geometric mean: 1.155x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x slower (HPT: reliability of 98.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x slower (HPT: reliability of 90.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base-mem.svg)
- [📄table](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.md)
- [📈time plot](bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0-vs-base.svg)

