# Results

- fork: python/7363476b6405e3d288a6
- version: 3.14.0a3+
- config: 
- commit hash: [7363476](https://github.com/python/cpython/commit/7363476)
- commit date: 2025-01-06T15:03:27-08:00
- commit merge base: [61c1a2478e6da8dc6dbdce4d6ac66b03d5963710](https://github.com/python/cpython/commit/61c1a2478e6da8dc6dbdce4d6ac66b03d5963710)
- ref: 7363476b6405e3d288a6

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.309x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250106-azure-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-pystats.json)
- [pystats table](bm-20250106-azure-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.106x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.345x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.83%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679835293)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.194x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x faster (HPT: reliability of 90.28%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679838132)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.154x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.163x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 56.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679534027)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

