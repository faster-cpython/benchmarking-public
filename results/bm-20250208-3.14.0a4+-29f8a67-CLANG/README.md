# Results

- fork: python/29f8a67ae00081a36fdc
- version: 3.14.0a4+
- config: CLANG
- commit hash: [29f8a67](https://github.com/python/cpython/commit/29f8a67)
- commit date: 2025-02-08T23:35:28+00:00
- commit merge base: [c1f352bf0813803bb795b796c16040a5cd4115f2](https://github.com/python/cpython/commit/c1f352bf0813803bb795b796c16040a5cd4115f2)
- ref: 29f8a67ae00081a36fdc

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.364x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.503x faster (HPT: reliability of 100.00%, 1.37x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.153x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.421x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.207x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x faster (HPT: reliability of 53.94%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x slower (HPT: reliability of 99.87%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 74.34%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.289x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.144x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.176x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.473x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.156x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.160x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

