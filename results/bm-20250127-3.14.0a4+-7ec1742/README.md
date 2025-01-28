# Results

- fork: python/7ec17429d462aee071c0
- version: 3.14.0a4+
- config: 
- commit hash: [7ec1742](https://github.com/python/cpython/commit/7ec1742)
- commit date: 2025-01-27T10:51:16+00:00
- commit merge base: [11148e91e3bee58ec1897ba3621445aa41629884](https://github.com/python/cpython/commit/11148e91e3bee58ec1897ba3621445aa41629884)
- ref: 7ec17429d462aee071c0

## linux x86_64 (azure)

- [pystats raw](bm-20250127-azure-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-pystats.json)
- [pystats table](bm-20250127-azure-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12993773120)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742.json)

### vs. 3.10.4

- Geometric mean: 1.436x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.10.4.md)
- [📈time plot](bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.12.0.md)
- [📈time plot](bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.13.0.md)
- [📈time plot](bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13009997240)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742.json)

### vs. 3.10.4

- Geometric mean: 1.359x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.10.4.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.12.0.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.13.0.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13014221946)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742.json)

### vs. 3.10.4

- Geometric mean: 1.398x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.10.4.md)
- [📈time plot](bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.12.0.md)
- [📈time plot](bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.100x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.13.0.md)
- [📈time plot](bm-20250127-darwin-arm64-python-7ec17429d462aee071c0-3.14.0a4%2B-7ec1742-vs-3.13.0.svg)

