# Results

- fork: python/359c7dde3bb074e02968
- version: 3.14.0a5+
- config: JIT
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

- Geometric mean: 1.273x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.002x faster (HPT: reliability of 72.22%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 89.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base-mem.svg)
- [📄table](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.445x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-linux-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 99.11%, 1.00x slower at 99th %ile)
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

- Geometric mean: 1.322x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 93.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 98.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base-mem.svg)
- [📄table](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-pythonperf2-x86_64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.265x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.075x faster (HPT: reliability of 98.91%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 82.32%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.031x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.064x faster (HPT: reliability of 92.10%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.069x faster (HPT: reliability of 99.08%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.033x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13349755371)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd.json)

### vs. 3.10.4

- Geometric mean: 1.365x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base-mem.svg)
- [📄table](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.md)
- [📈time plot](bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5%2B-359c7dd-vs-base.svg)

