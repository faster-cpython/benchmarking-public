# Results

- fork: python/f72977b2f4a29063ae30
- version: 3.14.0a4+
- config: JIT
- commit hash: [f72977b](https://github.com/python/cpython/commit/f72977b)
- commit date: 2025-02-09T06:13:43+00:00
- commit merge base: [29f8a67ae00081a36fdc97f2f2f96f971393a22a](https://github.com/python/cpython/commit/29f8a67ae00081a36fdc97f2f2f96f971393a22a)
- ref: f72977b2f4a29063ae30

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b.json)

### vs. 3.10.4

- Geometric mean: 1.270x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.md)
- [📈time plot](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.003x slower (HPT: reliability of 75.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.md)
- [📈time plot](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 81.66%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.md)
- [📈time plot](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 91.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base-mem.svg)
- [📄table](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.md)
- [📈time plot](bm-20250209-arminc-aarch64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250209-azure-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-pystats.json)
- [pystats table](bm-20250209-azure-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b.json)

### vs. 3.10.4

- Geometric mean: 1.448x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.md)
- [📈time plot](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.112x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.md)
- [📈time plot](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.md)
- [📈time plot](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 62.08%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base-mem.svg)
- [📄table](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.md)
- [📈time plot](bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b.json)

### vs. 3.10.4

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.md)
- [📈time plot](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 93.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.md)
- [📈time plot](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.md)
- [📈time plot](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 73.34%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base-mem.svg)
- [📄table](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.md)
- [📈time plot](bm-20250209-pythonperf2-x86_64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b.json)

### vs. 3.10.4

- Geometric mean: 1.261x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.md)
- [📈time plot](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 99.39%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.md)
- [📈time plot](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 65.70%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.md)
- [📈time plot](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.md)
- [📈time plot](bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b.json)

### vs. 3.10.4

- Geometric mean: 1.081x faster (HPT: reliability of 95.64%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.md)
- [📈time plot](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.md)
- [📈time plot](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.md)
- [📈time plot](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 99.35%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.md)
- [📈time plot](bm-20250209-pythonperf1_win32-x86-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b.json)

### vs. 3.10.4

- Geometric mean: 1.376x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.md)
- [📈time plot](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.080x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.md)
- [📈time plot](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.md)
- [📈time plot](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 84.96%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base-mem.svg)
- [📄table](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.md)
- [📈time plot](bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4%2B-f72977b-vs-base.svg)

