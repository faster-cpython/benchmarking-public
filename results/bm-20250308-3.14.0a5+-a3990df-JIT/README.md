# Results

- fork: python/a3990df6121880e8c678
- version: 3.14.0a5+
- config: JIT
- commit hash: [a3990df](https://github.com/python/cpython/commit/a3990df)
- commit date: 2025-03-08T16:37:05-05:00
- commit merge base: [edd1eca336976b3431cf636aea87f08a40c94935](https://github.com/python/cpython/commit/edd1eca336976b3431cf636aea87f08a40c94935)
- ref: a3990df6121880e8c678

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.318x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.74%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.449x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 80.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.324x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 97.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 98.07%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.254x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 94.02%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 90.62%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.022x faster (HPT: reliability of 84.03%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.052x faster (HPT: reliability of 73.08%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 98.17%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.065x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.371x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.081x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

