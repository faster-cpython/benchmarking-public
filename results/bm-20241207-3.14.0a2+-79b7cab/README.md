# Results

- fork: python/79b7cab50a3292a1c014
- version: 3.14.0a2+
- config: 
- commit hash: [79b7cab](https://github.com/python/cpython/commit/79b7cab)
- commit date: 2024-12-07T17:58:42+00:00
- commit merge base: [27d0d2141319d82709eb09ba20065df3e1714fab](https://github.com/python/cpython/commit/27d0d2141319d82709eb09ba20065df3e1714fab)
- ref: 79b7cab50a3292a1c014

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.308x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 86.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.45%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241207-azure-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-pystats.json)
- [pystats table](bm-20241207-azure-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12282170363)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.425x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x faster (HPT: reliability of 98.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.022x faster (HPT: reliability of 88.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.176x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.004x slower (HPT: reliability of 96.16%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.156x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.163x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 86.53%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.267x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

