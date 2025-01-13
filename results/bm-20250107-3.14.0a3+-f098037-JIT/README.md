# Results

- fork: brandtbucher/nojit
- version: 3.14.0a3+
- config: JIT
- commit hash: [f098037](https://github.com/brandtbucher/cpython/commit/f098037)
- commit date: 2025-01-07T14:31:59-08:00
- commit merge base: [7363476b6405e3d288a61282aa7bc6aca9c2114d](https://github.com/python/cpython/commit/7363476b6405e3d288a61282aa7bc6aca9c2114d)
- ref: nojit

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.220x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x slower (HPT: reliability of 99.50%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x slower (HPT: reliability of 95.71%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 95.01%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats.json)
- [pystats table](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats.md)

### vs. base

- [pystats diff](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.432x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.31%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 95.61%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.308x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.020x faster (HPT: reliability of 79.30%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 98.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 83.24%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.263x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.079x faster (HPT: reliability of 98.68%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 82.83%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 63.47%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.064x faster (HPT: reliability of 84.18%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.273x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.079x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 52.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

