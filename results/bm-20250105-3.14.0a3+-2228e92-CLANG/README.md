# Results

- fork: python/2228e92da31ca7344a16
- version: 3.14.0a3+
- config: CLANG
- commit hash: [2228e92](https://github.com/python/cpython/commit/2228e92)
- commit date: 2025-01-05T12:07:18+00:00
- commit merge base: [ae23a012e6c8aadc4a588101cbe7bc86ede45627](https://github.com/python/cpython/commit/ae23a012e6c8aadc4a588101cbe7bc86ede45627)
- ref: 2228e92da31ca7344a16

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12679934038)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.238x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x slower (HPT: reliability of 98.28%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x slower (HPT: reliability of 99.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.041x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: 🔴 mypy2
- [🧠memory plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base-mem.svg)
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12677798960)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.390x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 99.66%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 74.60%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.032x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 mypy2
- [🧠memory plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base-mem.svg)
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696190243)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.138x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x slower (HPT: reliability of 99.94%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.049x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696193623)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.250x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.255x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 mypy2
- [📄table](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12677795342)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.203x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x faster (HPT: reliability of 59.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.079x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: 🔴 mypy2
- [🧠memory plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base-mem.svg)
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

