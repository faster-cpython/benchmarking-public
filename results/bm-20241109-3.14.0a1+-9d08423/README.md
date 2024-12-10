# Results

- fork: python/9d08423b6e0fa89ce9cf
- version: 3.14.0a1+
- config: 
- commit hash: [9d08423](https://github.com/python/cpython/commit/9d08423)
- commit date: 2024-11-09T23:01:32+00:00
- commit merge base: [266328552e922fd9030cd699e10a25f03a67c8ba](https://github.com/python/cpython/commit/266328552e922fd9030cd699e10a25f03a67c8ba)
- ref: 9d08423b6e0fa89ce9cf

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.283x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.001x faster (HPT: reliability of 56.53%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 95.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241109-azure-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-pystats.json)
- [pystats table](bm-20241109-azure-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.402x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 82.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x faster (HPT: reliability of 94.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.164x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x slower (HPT: reliability of 99.58%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x faster (HPT: reliability of 99.73%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.246x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

