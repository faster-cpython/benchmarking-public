# Results

- fork: python/09d6f5dc7824c74672ad
- version: 3.14.0a1+
- config: JIT
- commit hash: [09d6f5d](https://github.com/python/cpython/commit/09d6f5d)
- commit date: 2024-11-07T10:55:31-08:00
- commit merge base: [a38e82bd8c249c126ab033c078170b6dea27a619](https://github.com/python/cpython/commit/a38e82bd8c249c126ab033c078170b6dea27a619)
- ref: 09d6f5dc7824c74672ad

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d.json)

### vs. 3.10.4

- Geometric mean: 1.166x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.md)
- [📈time plot](bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.083x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.md)
- [📈time plot](bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.md)
- [📈time plot](bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241107-azure-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-pystats.json)
- [pystats table](bm-20241107-azure-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d.json)

### vs. 3.10.4

- Geometric mean: 1.383x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.md)
- [📈time plot](bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.md)
- [📈time plot](bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x slower (HPT: reliability of 80.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.md)
- [📈time plot](bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d.json)

### vs. 3.10.4

- Geometric mean: 1.259x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.md)
- [📈time plot](bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x slower (HPT: reliability of 92.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.md)
- [📈time plot](bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 89.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.md)
- [📈time plot](bm-20241107-pythonperf2-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d.json)

### vs. 3.10.4

- Geometric mean: 1.212x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.md)
- [📈time plot](bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 83.20%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.md)
- [📈time plot](bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x faster (HPT: reliability of 88.28%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.md)
- [📈time plot](bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d.json)

### vs. 3.10.4

- Geometric mean: 1.037x faster (HPT: reliability of 62.41%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.md)
- [📈time plot](bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 98.88%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.md)
- [📈time plot](bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.md)
- [📈time plot](bm-20241107-pythonperf1_win32-x86-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d.json)

### vs. 3.10.4

- Geometric mean: 1.211x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.44x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.md)
- [📈time plot](bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 81.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.md)
- [📈time plot](bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x faster (HPT: reliability of 80.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.md)
- [📈time plot](bm-20241107-darwin-arm64-python-09d6f5dc7824c74672ad-3.14.0a1%2B-09d6f5d-vs-3.13.0.svg)

