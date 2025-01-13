# Results

- fork: python/615abb99a4538520f380
- version: 3.14.0a2+
- config: JIT
- commit hash: [615abb9](https://github.com/python/cpython/commit/615abb9)
- commit date: 2024-11-22T15:30:01+00:00
- commit merge base: [0cb4d6c6549d2299f7518f083bbe7d10314ecd66](https://github.com/python/cpython/commit/0cb4d6c6549d2299f7518f083bbe7d10314ecd66)
- ref: 615abb99a4538520f380

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9.json)

### vs. 3.10.4

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.md)
- [📈time plot](bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.md)
- [📈time plot](bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.md)
- [📈time plot](bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241122-azure-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-pystats.json)
- [pystats table](bm-20241122-azure-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9.json)

### vs. 3.10.4

- Geometric mean: 1.410x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.md)
- [📈time plot](bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.md)
- [📈time plot](bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 77.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.md)
- [📈time plot](bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9.json)

### vs. 3.10.4

- Geometric mean: 1.278x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 89.38%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x slower (HPT: reliability of 82.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.md)
- [📈time plot](bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9.json)

### vs. 3.10.4

- Geometric mean: 1.232x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.md)
- [📈time plot](bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 94.49%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.md)
- [📈time plot](bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x faster (HPT: reliability of 94.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.md)
- [📈time plot](bm-20241122-pythonperf1-amd64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2%2B-615abb9.json)

### vs. 3.10.4

- Geometric mean: 1.051x faster (HPT: reliability of 70.73%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.md)
- [📈time plot](bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 99.93%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.md)
- [📈time plot](bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.md)
- [📈time plot](bm-20241122-pythonperf1_win32-x86-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11975780307)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9.json)

### vs. 3.10.4

- Geometric mean: 1.230x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.md)
- [📈time plot](bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 97.16%, 1.00x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.md)
- [📈time plot](bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.md)
- [📈time plot](bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2%2B-615abb9-vs-3.13.0.svg)

