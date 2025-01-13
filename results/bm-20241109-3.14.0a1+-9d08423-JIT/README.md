# Results

- fork: python/9d08423b6e0fa89ce9cf
- version: 3.14.0a1+
- config: JIT
- commit hash: [9d08423](https://github.com/python/cpython/commit/9d08423)
- commit date: 2024-11-09T23:01:32+00:00
- commit merge base: [266328552e922fd9030cd699e10a25f03a67c8ba](https://github.com/python/cpython/commit/266328552e922fd9030cd699e10a25f03a67c8ba)
- ref: 9d08423b6e0fa89ce9cf

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.159x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.082x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.379x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 84.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x slower (HPT: reliability of 97.06%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.277x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 84.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 66.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x slower (HPT: reliability of 96.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.208x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.019x faster (HPT: reliability of 87.60%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 97.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.035x faster (HPT: reliability of 96.29%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.039x faster (HPT: reliability of 52.28%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.68%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.072x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.216x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.44x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, many_optionals, subparsers, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x faster (HPT: reliability of 85.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 90.15%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.019x slower (HPT: reliability of 99.54%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

