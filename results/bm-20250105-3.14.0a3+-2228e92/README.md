# Results

- fork: python/2228e92da31ca7344a16
- version: 3.14.0a3+
- config: 
- commit hash: [2228e92](https://github.com/python/cpython/commit/2228e92)
- commit date: 2025-01-05T12:07:18+00:00
- commit merge base: [ae23a012e6c8aadc4a588101cbe7bc86ede45627](https://github.com/python/cpython/commit/ae23a012e6c8aadc4a588101cbe7bc86ede45627)
- ref: 2228e92da31ca7344a16

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.303x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x faster (HPT: reliability of 95.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.343x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12712222122)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 90.70%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.170x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.180x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x faster (HPT: reliability of 72.89%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

