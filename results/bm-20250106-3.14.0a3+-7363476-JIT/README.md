# Results

- fork: python/7363476b6405e3d288a6
- version: 3.14.0a3+
- config: JIT
- commit hash: [7363476](https://github.com/python/cpython/commit/7363476)
- commit date: 2025-01-06T15:03:27-08:00
- commit merge base: [61c1a2478e6da8dc6dbdce4d6ac66b03d5963710](https://github.com/python/cpython/commit/61c1a2478e6da8dc6dbdce4d6ac66b03d5963710)
- ref: 7363476b6405e3d288a6

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.224x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x slower (HPT: reliability of 99.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x slower (HPT: reliability of 96.74%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.057x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.02x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base-mem.svg)
- [📄table](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.md)
- [📈time plot](bm-20250106-arminc-aarch64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250106-azure-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-pystats.json)
- [pystats table](bm-20250106-azure-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-pystats.md)

### vs. base

- [pystats diff](bm-20250106-azure-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 87.68%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base-mem.svg)
- [📄table](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.md)
- [📈time plot](bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.310x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.022x faster (HPT: reliability of 77.22%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 97.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.023x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base-mem.svg)
- [📄table](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.md)
- [📈time plot](bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.260x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 98.53%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 76.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.051x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- new benchmarks: mypy2
- [📄table](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.md)
- [📈time plot](bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.059x faster (HPT: reliability of 77.42%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.079x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: mypy2
- [📄table](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.md)
- [📈time plot](bm-20250106-pythonperf1_win32-x86-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476.json)

### vs. 3.10.4

- Geometric mean: 1.269x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.md)
- [📈time plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.md)
- [📈time plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.md)
- [📈time plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.030x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.02x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base-mem.svg)
- [📄table](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.md)
- [📈time plot](bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3%2B-7363476-vs-base.svg)

