# Results

- fork: python/29f8a67ae00081a36fdc
- version: 3.14.0a4+
- config: JIT
- commit hash: [29f8a67](https://github.com/python/cpython/commit/29f8a67)
- commit date: 2025-02-08T23:35:28+00:00
- commit merge base: [c1f352bf0813803bb795b796c16040a5cd4115f2](https://github.com/python/cpython/commit/c1f352bf0813803bb795b796c16040a5cd4115f2)
- ref: 29f8a67ae00081a36fdc

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13220395690)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.273x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.002x slower (HPT: reliability of 73.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 79.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13220395690)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.447x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13220395690)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.329x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 73.35%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13220395690)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.248x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 97.95%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 86.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x faster (HPT: reliability of 76.86%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13220395690)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.079x faster (HPT: reliability of 97.38%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 93.66%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13220395690)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.377x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 99.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

