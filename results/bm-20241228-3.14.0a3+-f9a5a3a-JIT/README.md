# Results

- fork: python/f9a5a3a3ef34e63dc197
- version: 3.14.0a3+
- config: JIT
- commit hash: [f9a5a3a](https://github.com/python/cpython/commit/f9a5a3a)
- commit date: 2024-12-28T21:05:34+00:00
- commit merge base: [492b224b991cd9027f1bc6d9988d01e94f764992](https://github.com/python/cpython/commit/492b224b991cd9027f1bc6d9988d01e94f764992)
- ref: f9a5a3a3ef34e63dc197

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.217x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x slower (HPT: reliability of 99.68%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x slower (HPT: reliability of 97.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.057x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base-mem.svg)
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.106x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 97.34%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 84.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base-mem.svg)
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.302x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 69.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 97.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base-mem.svg)
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.248x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x faster (HPT: reliability of 97.93%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 56.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.053x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.055x faster (HPT: reliability of 74.06%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 99.93%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.094x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-pythonperf1_win32-x86-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

