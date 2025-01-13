# Results

- fork: python/0ac40acec045c4ce780c
- version: 3.14.0a2+
- config: NOGIL
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

- Geometric mean: 1.109x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.294x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.285x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.309x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.077x faster (HPT: reliability of 99.91%, 1.01x faster at 99th %ile)
- Memory usage: 1.49x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.167x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.210x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.235x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.005x faster (HPT: reliability of 69.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.217x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.199x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.235x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12334101588)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac.json)

### vs. 3.10.4

- Geometric mean: 1.025x faster (HPT: reliability of 74.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.132x slower (HPT: reliability of 99.85%, 1.02x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.109x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.176x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.13x
- [🧠memory plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base-mem.svg)
- [📄table](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.md)
- [📈time plot](bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2%2B-0ac40ac-vs-base.svg)

