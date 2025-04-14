# Results

- fork: python/5ec4bf86b7f4455432ae
- version: 3.14.0a5+
- config: CLANG
- commit hash: [5ec4bf8](https://github.com/python/cpython/commit/5ec4bf8)
- commit date: 2025-02-22T17:54:43+00:00
- commit merge base: [3cc9e867eba1ed139cf28c74b4a788bcc4801394](https://github.com/python/cpython/commit/3cc9e867eba1ed139cf28c74b4a788bcc4801394)
- ref: 5ec4bf86b7f4455432ae

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8.json)

### vs. 3.10.4

- Geometric mean: 1.355x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.md)
- [📈time plot](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.md)
- [📈time plot](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.md)
- [📈time plot](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base-mem.svg)
- [📄table](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.md)
- [📈time plot](bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8.json)

### vs. 3.10.4

- Geometric mean: 1.489x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.md)
- [📈time plot](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.144x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.md)
- [📈time plot](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.074x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.md)
- [📈time plot](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.026x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base-mem.svg)
- [📄table](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.md)
- [📈time plot](bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8.json)

### vs. 3.10.4

- Geometric mean: 1.412x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.093x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base-mem.svg)
- [📄table](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.md)
- [📈time plot](bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8.json)

### vs. 3.10.4

- Geometric mean: 1.231x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.md)
- [📈time plot](bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x faster (HPT: reliability of 70.57%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.md)
- [📈time plot](bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 99.52%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.md)
- [📈time plot](bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8.json)

### vs. 3.10.4

- Geometric mean: 1.286x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.md)
- [📈time plot](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.md)
- [📈time plot](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.146x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.md)
- [📈time plot](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.md)
- [📈time plot](bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13525064046)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8.json)

### vs. 3.10.4

- Geometric mean: 1.473x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.md)
- [📈time plot](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.156x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.md)
- [📈time plot](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.160x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.md)
- [📈time plot](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.170x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base-mem.svg)
- [📄table](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.md)
- [📈time plot](bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5%2B-5ec4bf8-vs-base.svg)

