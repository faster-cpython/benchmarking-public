# Results

- fork: python/1953713d0d67a4f54ff7
- version: 3.15.0a0
- config: NOGIL
- commit hash: [1953713](https://github.com/python/cpython/commit/1953713)
- commit date: 2025-07-05T15:54:26-07:00
- commit merge base: [5dac137b9f75c5c1d5096101bcd33d565d0526e4](https://github.com/python/cpython/commit/5dac137b9f75c5c1d5096101bcd33d565d0526e4)
- ref: 1953713d0d67a4f54ff7

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.142x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.67x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x slower (HPT: reliability of 99.76%, 1.01x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.090x slower (HPT: reliability of 99.89%, 1.01x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.126x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base-mem.svg)
- [📄table](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.md)
- [📈time plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.190x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.66x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x slower (HPT: reliability of 99.03%, 1.00x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x slower (HPT: reliability of 98.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.093x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base-mem.svg)
- [📄table](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.md)
- [📈time plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.135x faster (HPT: reliability of 99.82%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x slower (HPT: reliability of 98.87%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.122x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.md)
- [📈time plot](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.318x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.127x faster (HPT: reliability of 99.57%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.121x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.md)
- [📈time plot](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.184x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x slower (HPT: reliability of 99.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x slower (HPT: reliability of 98.94%, 1.00x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.037x slower (HPT: reliability of 99.94%, 1.01x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base-mem.svg)
- [📄table](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.md)
- [📈time plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-base.svg)

