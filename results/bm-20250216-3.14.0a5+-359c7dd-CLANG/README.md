# Results

- fork: python/359c7dde3bb074e02968
- version: 3.14.0a5+
- config: CLANG
- commit hash: [359c7dd](https://github.com/python/cpython/commit/359c7dd)
- commit date: 2025-02-16T03:01:24+08:00
- commit merge base: [c26bed1160978fe8b1844878b8123778e47870c6](https://github.com/python/cpython/commit/c26bed1160978fe8b1844878b8123778e47870c6)
- ref: 359c7dde3bb074e02968

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.343x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base-mem.svg)
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.494x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.145x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.075x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.030x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base-mem.svg)
- [📄table](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.401x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base-mem.svg)
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.235x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 81.49%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 98.91%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 85.91%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.283x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.286x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.144x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.165x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.466x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.150x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.154x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.168x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base-mem.svg)
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

