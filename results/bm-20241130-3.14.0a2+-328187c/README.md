# Results

- fork: python/328187cc4fcdd578db42
- version: 3.14.0a2+
- config: 
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

- Geometric mean: 1.297x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x faster (HPT: reliability of 63.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.000x slower (HPT: reliability of 81.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.405x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 78.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.303x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.002x faster (HPT: reliability of 61.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 92.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.162x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x slower (HPT: reliability of 99.84%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.148x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.150x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 86.99%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.242x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

