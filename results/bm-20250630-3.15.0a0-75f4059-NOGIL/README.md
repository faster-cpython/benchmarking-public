# Results

- fork: python/75f40595e555e7d016cf
- version: 3.15.0a0
- config: NOGIL
- commit hash: [75f4059](https://github.com/python/cpython/commit/75f4059)
- commit date: 2025-06-30T09:32:51-04:00
- commit merge base: [847d1c2cb4014f122df64e0db0b3b554c01779c6](https://github.com/python/cpython/commit/847d1c2cb4014f122df64e0db0b3b554c01779c6)
- ref: 75f40595e555e7d016cf

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15974405296)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json)

### vs. 3.10.4

- Geometric mean: 1.185x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.66x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.md)
- [📈time plot](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.056x slower (HPT: reliability of 99.69%, 1.01x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.md)
- [📈time plot](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x slower (HPT: reliability of 99.84%, 1.01x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.md)
- [📈time plot](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.121x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base-mem.svg)
- [📄table](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.md)
- [📈time plot](bm-20250630-arminc-aarch64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15974405296)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json)

### vs. 3.10.4

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.md)
- [📈time plot](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.005x faster (HPT: reliability of 79.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.md)
- [📈time plot](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x slower (HPT: reliability of 99.92%, 1.01x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.md)
- [📈time plot](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base-mem.svg)
- [📄table](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.md)
- [📈time plot](bm-20250630-linux-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15974405296)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json)

### vs. 3.10.4

- Geometric mean: 1.241x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.64x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.md)
- [📈time plot](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x slower (HPT: reliability of 98.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.md)
- [📈time plot](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x slower (HPT: reliability of 93.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.md)
- [📈time plot](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base-mem.svg)
- [📄table](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.md)
- [📈time plot](bm-20250630-pythonperf2-x86_64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15974405296)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json)

### vs. 3.10.4

- Geometric mean: 1.132x faster (HPT: reliability of 99.68%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.md)
- [📈time plot](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x slower (HPT: reliability of 99.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.md)
- [📈time plot](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x slower (HPT: reliability of 99.98%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.md)
- [📈time plot](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.125x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.md)
- [📈time plot](bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15974405296)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json)

### vs. 3.10.4

- Geometric mean: 1.271x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.md)
- [📈time plot](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.md)
- [📈time plot](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.115x faster (HPT: reliability of 98.49%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.md)
- [📈time plot](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.129x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.md)
- [📈time plot](bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15974405296)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json)

### vs. 3.10.4

- Geometric mean: 1.341x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.md)
- [📈time plot](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 95.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.md)
- [📈time plot](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.md)
- [📈time plot](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base-mem.svg)
- [📄table](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.md)
- [📈time plot](bm-20250630-darwin-arm64-python-75f40595e555e7d016cf-3.15.0a0-75f4059-vs-base.svg)

