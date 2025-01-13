# Results

- fork: python/c695e37a3f95c225ee08
- version: 3.14.0a1+
- config: JIT
- commit hash: [c695e37](https://github.com/python/cpython/commit/c695e37)
- commit date: 2024-11-13T21:39:10+00:00
- commit merge base: [f6b0361c17552197f44be16435e4a5cb4b1d60ca](https://github.com/python/cpython/commit/f6b0361c17552197f44be16435e4a5cb4b1d60ca)
- ref: c695e37a3f95c225ee08

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37.json)

### vs. 3.10.4

- Geometric mean: 1.158x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.md)
- [📈time plot](bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.md)
- [📈time plot](bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.md)
- [📈time plot](bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241113-azure-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-pystats.json)
- [pystats table](bm-20241113-azure-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37.json)

### vs. 3.10.4

- Geometric mean: 1.378x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.md)
- [📈time plot](bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.md)
- [📈time plot](bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 93.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.md)
- [📈time plot](bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37.json)

### vs. 3.10.4

- Geometric mean: 1.259x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x slower (HPT: reliability of 96.32%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 95.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37.json)

### vs. 3.10.4

- Geometric mean: 1.207x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.md)
- [📈time plot](bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.020x faster (HPT: reliability of 89.46%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.md)
- [📈time plot](bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x slower (HPT: reliability of 95.06%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.md)
- [📈time plot](bm-20241113-pythonperf1-amd64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37.json)

### vs. 3.10.4

- Geometric mean: 1.036x faster (HPT: reliability of 67.03%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.md)
- [📈time plot](bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 98.88%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.md)
- [📈time plot](bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.md)
- [📈time plot](bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37.json)

### vs. 3.10.4

- Geometric mean: 1.212x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.44x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, many_optionals, subparsers, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.md)
- [📈time plot](bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x faster (HPT: reliability of 90.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.md)
- [📈time plot](bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 85.45%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.md)
- [📈time plot](bm-20241113-darwin-arm64-python-c695e37a3f95c225ee08-3.14.0a1%2B-c695e37-vs-3.13.0.svg)

