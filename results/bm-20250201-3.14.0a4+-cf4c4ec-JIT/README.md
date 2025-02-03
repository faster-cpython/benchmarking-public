# Results

- fork: python/cf4c4ecc26c7e3b89f2e
- version: 3.14.0a4+
- config: JIT
- commit hash: [cf4c4ec](https://github.com/python/cpython/commit/cf4c4ec)
- commit date: 2025-02-01T18:49:45+02:00
- commit merge base: [71ae93374defd192e5e88fe0912eff4f8e56f286](https://github.com/python/cpython/commit/71ae93374defd192e5e88fe0912eff4f8e56f286)
- ref: cf4c4ecc26c7e3b89f2e

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.217x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x slower (HPT: reliability of 98.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x slower (HPT: reliability of 93.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.074x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base-mem.svg)
- [📄table](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.06%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 78.19%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base-mem.svg)
- [📄table](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.316x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 80.07%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.037x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base-mem.svg)
- [📄table](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.278x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 99.79%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 53.29%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x faster (HPT: reliability of 91.28%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.039x faster (HPT: reliability of 59.16%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.050x faster (HPT: reliability of 98.60%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.075x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13093635868)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec.json)

### vs. 3.10.4

- Geometric mean: 1.352x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.md)
- [📈time plot](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.md)
- [📈time plot](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.md)
- [📈time plot](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.041x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base-mem.svg)
- [📄table](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.md)
- [📈time plot](bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4%2B-cf4c4ec-vs-base.svg)

