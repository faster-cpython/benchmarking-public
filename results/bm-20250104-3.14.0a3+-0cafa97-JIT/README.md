# Results

- fork: python/0cafa97932c6574734bb
- version: 3.14.0a3+
- config: JIT
- commit hash: [0cafa97](https://github.com/python/cpython/commit/0cafa97)
- commit date: 2025-01-04T23:38:46+00:00
- commit merge base: [e8b6b39ff707378da654e15ccddde9c28cefdd30](https://github.com/python/cpython/commit/e8b6b39ff707378da654e15ccddde9c28cefdd30)
- ref: 0cafa97932c6574734bb

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.224x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x slower (HPT: reliability of 99.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 98.08%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.052x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 98.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 98.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.303x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 58.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 97.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.253x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 97.59%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 66.15%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.037x faster (HPT: reliability of 99.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.071x faster (HPT: reliability of 93.20%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.083x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.074x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.275x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

