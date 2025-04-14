# Results

- fork: python/v3.14.0a5
- version: 3.14.0a5
- config: JIT
- commit hash: [3ae9101](https://github.com/python/cpython/commit/3ae9101)
- commit date: 2025-02-11T19:16:29+02:00
- commit merge base: [5cdd6e5e758a3fc0a5daac80753bf611b3e23c2d](https://github.com/python/cpython/commit/5cdd6e5e758a3fc0a5daac80753bf611b3e23c2d)
- ref: v3.14.0a5

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101.json)

### vs. 3.10.4

- Geometric mean: 1.275x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.md)
- [📈time plot](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.005x faster (HPT: reliability of 80.30%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.md)
- [📈time plot](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 92.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.md)
- [📈time plot](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 95.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base-mem.svg)
- [📄table](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.md)
- [📈time plot](bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250211-azure-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-pystats.json)
- [pystats table](bm-20250211-azure-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-pystats.md)

### vs. base

- [pystats diff](bm-20250211-azure-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101.json)

### vs. 3.10.4

- Geometric mean: 1.443x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.md)
- [📈time plot](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.md)
- [📈time plot](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.md)
- [📈time plot](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 75.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base-mem.svg)
- [📄table](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.md)
- [📈time plot](bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101.json)

### vs. 3.10.4

- Geometric mean: 1.331x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.md)
- [📈time plot](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 96.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.md)
- [📈time plot](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.md)
- [📈time plot](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 94.35%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base-mem.svg)
- [📄table](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.md)
- [📈time plot](bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101.json)

### vs. 3.10.4

- Geometric mean: 1.248x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.md)
- [📈time plot](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 93.26%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.md)
- [📈time plot](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 83.14%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.md)
- [📈time plot](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 80.04%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.md)
- [📈time plot](bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101.json)

### vs. 3.10.4

- Geometric mean: 1.075x faster (HPT: reliability of 87.35%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.md)
- [📈time plot](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.080x faster (HPT: reliability of 99.72%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.md)
- [📈time plot](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.md)
- [📈time plot](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.md)
- [📈time plot](bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101.json)

### vs. 3.10.4

- Geometric mean: 1.302x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.md)
- [📈time plot](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.022x faster (HPT: reliability of 79.53%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.md)
- [📈time plot](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 99.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.md)
- [📈time plot](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.054x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base-mem.svg)
- [📄table](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.md)
- [📈time plot](bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101-vs-base.svg)

