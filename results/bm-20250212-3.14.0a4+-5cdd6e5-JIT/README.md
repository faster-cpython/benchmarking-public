# Results

- fork: python/5cdd6e5e758a3fc0a5da
- version: 3.14.0a4+
- config: JIT
- commit hash: [5cdd6e5](https://github.com/python/cpython/commit/5cdd6e5)
- commit date: 2025-02-12T01:13:05+08:00
- commit merge base: [3b548adc765a83bedc316b19cb922a02c7a201f1](https://github.com/python/cpython/commit/3b548adc765a83bedc316b19cb922a02c7a201f1)
- ref: 5cdd6e5e758a3fc0a5da

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5.json)

### vs. 3.10.4

- Geometric mean: 1.274x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.md)
- [📈time plot](bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.003x faster (HPT: reliability of 82.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.md)
- [📈time plot](bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 87.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.md)
- [📈time plot](bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250212-azure-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-pystats.json)
- [pystats table](bm-20250212-azure-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5.json)

### vs. 3.10.4

- Geometric mean: 1.447x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.md)
- [📈time plot](bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.md)
- [📈time plot](bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.md)
- [📈time plot](bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5.json)

### vs. 3.10.4

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.md)
- [📈time plot](bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 95.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.md)
- [📈time plot](bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.md)
- [📈time plot](bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5.json)

### vs. 3.10.4

- Geometric mean: 1.247x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.md)
- [📈time plot](bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 95.38%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.md)
- [📈time plot](bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x faster (HPT: reliability of 83.84%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.md)
- [📈time plot](bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5.json)

### vs. 3.10.4

- Geometric mean: 1.089x faster (HPT: reliability of 95.11%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.md)
- [📈time plot](bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.097x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.md)
- [📈time plot](bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.md)
- [📈time plot](bm-20250212-pythonperf1_win32-x86-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13461534459)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5.json)

### vs. 3.10.4

- Geometric mean: 1.376x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.md)
- [📈time plot](bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.080x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.md)
- [📈time plot](bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.md)
- [📈time plot](bm-20250212-darwin-arm64-python-5cdd6e5e758a3fc0a5da-3.14.0a4%2B-5cdd6e5-vs-3.13.0.svg)

