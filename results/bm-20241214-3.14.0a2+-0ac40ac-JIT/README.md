# Results

- fork: python/0ac40acec045c4ce780c
- version: 3.14.0a2+
- config: JIT
- commit hash: [0ac40ac](https://github.com/python/cpython/commit/0ac40ac)
- commit date: 2024-12-14T17:25:49+02:00
- commit merge base: [e2325c9db0650fc06d909eb2b5930c0573f24f71](https://github.com/python/cpython/commit/e2325c9db0650fc06d909eb2b5930c0573f24f71)
- ref: 0ac40acec045c4ce780c

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.226x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x slower (HPT: reliability of 99.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 90.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.047x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 95.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 63.50%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.303x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 52.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 92.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.253x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 97.50%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 62.09%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.048x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.063x faster (HPT: reliability of 87.66%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.082x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.248x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 92.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

