# Results

- fork: brandtbucher/nojit
- version: 3.14.0a3+
- config: 
- commit hash: [f098037](https://github.com/brandtbucher/cpython/commit/f098037)
- commit date: 2025-01-07T14:31:59-08:00
- commit merge base: [7363476b6405e3d288a61282aa7bc6aca9c2114d](https://github.com/python/cpython/commit/7363476b6405e3d288a61282aa7bc6aca9c2114d)
- ref: nojit

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12674557620)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.311x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.033x faster (HPT: reliability of 96.07%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 82.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats.json)
- [pystats table](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats.md)

### vs. base

- [pystats diff](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12674557620)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 93.52%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12674557620)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.347x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 93.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12674557620)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.209x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x faster (HPT: reliability of 55.64%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 99.56%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12674557620)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.153x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.162x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 93.04%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12674557620)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.316x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 85.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- new benchmarks: mypy2
- [🧠memory plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

