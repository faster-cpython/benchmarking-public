# Results

- fork: python/79b7cab50a3292a1c014
- version: 3.14.0a2+
- config: JIT
- commit hash: [79b7cab](https://github.com/python/cpython/commit/79b7cab)
- commit date: 2024-12-07T17:58:42+00:00
- commit merge base: [27d0d2141319d82709eb09ba20065df3e1714fab](https://github.com/python/cpython/commit/27d0d2141319d82709eb09ba20065df3e1714fab)
- ref: 79b7cab50a3292a1c014

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.231x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x slower (HPT: reliability of 99.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x slower (HPT: reliability of 93.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.054x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.441x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.52%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 95.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: 🔴 mypy2
- [🧠memory plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.296x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.008x faster (HPT: reliability of 77.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x faster (HPT: reliability of 91.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x slower (HPT: reliability of 99.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.256x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x faster (HPT: reliability of 99.82%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 79.01%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.060x faster (HPT: reliability of 89.93%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.080x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.243x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 99.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x slower (HPT: reliability of 98.50%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

