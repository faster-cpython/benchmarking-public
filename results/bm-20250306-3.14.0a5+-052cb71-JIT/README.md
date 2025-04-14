# Results

- fork: python/052cb717f5f97d08d207
- version: 3.14.0a5+
- config: JIT
- commit hash: [052cb71](https://github.com/python/cpython/commit/052cb71)
- commit date: 2025-03-06T10:38:34-05:00
- commit merge base: [c6dd2348ca61436fc1444ecc0343cb24932f6fa7](https://github.com/python/cpython/commit/c6dd2348ca61436fc1444ecc0343cb24932f6fa7)
- ref: 052cb717f5f97d08d207

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.md)
- [📈time plot](bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.md)
- [📈time plot](bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.md)
- [📈time plot](bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71.json)

### vs. 3.10.4

- Geometric mean: 1.444x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.md)
- [📈time plot](bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.md)
- [📈time plot](bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.md)
- [📈time plot](bm-20250306-linux-x86_64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71.json)

### vs. 3.10.4

- Geometric mean: 1.239x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.md)
- [📈time plot](bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 84.20%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.md)
- [📈time plot](bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x faster (HPT: reliability of 95.84%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.md)
- [📈time plot](bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13720004889)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71.json)

### vs. 3.10.4

- Geometric mean: 1.370x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.md)
- [📈time plot](bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.md)
- [📈time plot](bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.md)
- [📈time plot](bm-20250306-darwin-arm64-python-052cb717f5f97d08d207-3.14.0a5%2B-052cb71-vs-3.13.0.svg)

