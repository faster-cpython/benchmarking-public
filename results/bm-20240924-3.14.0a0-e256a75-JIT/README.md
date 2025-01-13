# Results

- fork: brandtbucher/main
- version: 3.14.0a0
- config: JIT
- commit hash: [e256a75](https://github.com/brandtbucher/cpython/commit/e256a75)
- commit date: 2024-09-24T02:47:05+03:00
- commit merge base: [38a887dc3ec52c4a7222279bf4b3ca2431b86de9](https://github.com/python/cpython/commit/38a887dc3ec52c4a7222279bf4b3ca2431b86de9)
- ref: main

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11004744804)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75.json)

### vs. 3.10.4

- Geometric mean: 1.175x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.md)
- [📈time plot](bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.076x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.md)
- [📈time plot](bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.083x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.md)
- [📈time plot](bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240924-azure-x86_64-brandtbucher-main-3.14.0a0-e256a75-pystats.json)
- [pystats table](bm-20240924-azure-x86_64-brandtbucher-main-3.14.0a0-e256a75-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11004744804)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.md)
- [📈time plot](bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.md)
- [📈time plot](bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 88.83%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.md)
- [📈time plot](bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11004744804)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75.json)

### vs. 3.10.4

- Geometric mean: 1.312x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.md)
- [📈time plot](bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 71.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.md)
- [📈time plot](bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 92.45%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.md)
- [📈time plot](bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11004744804)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75.json)

### vs. 3.10.4

- Geometric mean: 1.238x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.md)
- [📈time plot](bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.049x faster (HPT: reliability of 88.74%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.md)
- [📈time plot](bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 97.49%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.md)
- [📈time plot](bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11004744804)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75.json)

### vs. 3.10.4

- Geometric mean: 1.233x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.md)
- [📈time plot](bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.244x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.md)
- [📈time plot](bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.116x faster (HPT: reliability of 98.91%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.md)
- [📈time plot](bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11004744804)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75.json)

### vs. 3.10.4

- Geometric mean: 1.240x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 0.72x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.md)
- [📈time plot](bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.049x faster (HPT: reliability of 98.42%, 1.00x faster at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.md)
- [📈time plot](bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.54x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.md)
- [📈time plot](bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75-vs-3.13.0.svg)

