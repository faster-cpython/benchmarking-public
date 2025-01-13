# Results

- fork: python/0cafa97932c6574734bb
- version: 3.14.0a3+
- config: NOGIL
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

- Geometric mean: 1.059x slower (HPT: reliability of 99.98%, 1.03x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.253x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.248x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.272x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.117x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.182x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.216x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-linux-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.052x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.179x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.163x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.208x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-pythonperf2-x86_64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12614751886)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x slower (HPT: reliability of 99.45%, 1.00x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x slower (HPT: reliability of 99.82%, 1.01x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.167x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.13x
- [🧠memory plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base-mem.svg)
- [📄table](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-darwin-arm64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

