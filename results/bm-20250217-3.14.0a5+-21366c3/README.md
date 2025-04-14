# Results

- fork: faster-cpython/c_recursion_limit
- version: 3.14.0a5+
- config: 
- commit hash: [21366c3](https://github.com/faster%2dcpython/cpython/commit/21366c3)
- commit date: 2025-02-17T09:44:33+00:00
- commit merge base: [1775091dc163d1fa76c33b01b9c82dc2430ffac8](https://github.com/python/cpython/commit/1775091dc163d1fa76c33b01b9c82dc2430ffac8)
- ref: c_recursion_limit

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.md)
- [📈time plot](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.md)
- [📈time plot](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.md)
- [📈time plot](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base-mem.svg)
- [📄table](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.md)
- [📈time plot](bm-20250217-arminc-aarch64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3.json)

### vs. 3.10.4

- Geometric mean: 1.452x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.md)
- [📈time plot](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.115x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.md)
- [📈time plot](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.md)
- [📈time plot](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 97.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base-mem.svg)
- [📄table](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.md)
- [📈time plot](bm-20250217-linux-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3.json)

### vs. 3.10.4

- Geometric mean: 1.354x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.md)
- [📈time plot](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.048x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.md)
- [📈time plot](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.md)
- [📈time plot](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 77.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base-mem.svg)
- [📄table](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.md)
- [📈time plot](bm-20250217-pythonperf2-x86_64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3.json)

### vs. 3.10.4

- Geometric mean: 1.245x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.md)
- [📈time plot](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x faster (HPT: reliability of 76.84%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.md)
- [📈time plot](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x faster (HPT: reliability of 99.76%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.md)
- [📈time plot](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 61.17%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.md)
- [📈time plot](bm-20250217-pythonperf1-amd64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3.json)

### vs. 3.10.4

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.md)
- [📈time plot](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.128x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.md)
- [📈time plot](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.000x faster (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.md)
- [📈time plot](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.md)
- [📈time plot](bm-20250217-pythonperf1_win32-x86-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13367754756)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3.json)

### vs. 3.10.4

- Geometric mean: 1.255x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.md)
- [📈time plot](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x slower (HPT: reliability of 99.30%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.md)
- [📈time plot](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 79.44%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.md)
- [📈time plot](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base-mem.svg)
- [📄table](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.md)
- [📈time plot](bm-20250217-darwin-arm64-faster%252dcpython-c_recursion_limit-3.14.0a5%2B-21366c3-vs-base.svg)

