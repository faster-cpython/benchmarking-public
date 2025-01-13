# Results

- fork: python/22a442181d5f1ac496da
- version: 3.14.0a3+
- config: 
- commit hash: [22a4421](https://github.com/python/cpython/commit/22a4421)
- commit date: 2025-01-11T19:27:47+00:00
- commit merge base: [0946ed25b53dddfa4eb040513720353b7214d71b](https://github.com/python/cpython/commit/0946ed25b53dddfa4eb040513720353b7214d71b)
- ref: 22a442181d5f1ac496da

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250111-azure-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-pystats.json)
- [pystats table](bm-20250111-azure-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.445x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.112x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.350x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.221x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 51.52%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.156x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.166x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 89.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.122x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

