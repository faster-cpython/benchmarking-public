# Results

- fork: python/328187cc4fcdd578db42
- version: 3.14.0a2+
- config: JIT
- commit hash: [328187c](https://github.com/python/cpython/commit/328187c)
- commit date: 2024-11-30T18:39:39+00:00
- commit merge base: [4e0a4cafe8d8ecb43db62aed1d5671af583104e7](https://github.com/python/cpython/commit/4e0a4cafe8d8ecb43db62aed1d5671af583104e7)
- ref: 328187cc4fcdd578db42

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.207x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x slower (HPT: reliability of 99.95%, 1.01x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.060x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.410x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 78.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 89.03%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.283x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 84.19%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 70.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 99.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.231x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 94.08%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 92.79%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.053x faster (HPT: reliability of 99.34%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.044x faster (HPT: reliability of 60.70%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.054x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.088x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.221x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 93.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x faster (HPT: reliability of 89.83%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x slower (HPT: reliability of 99.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

