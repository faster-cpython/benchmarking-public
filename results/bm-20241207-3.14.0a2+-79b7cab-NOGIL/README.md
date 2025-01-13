# Results

- fork: python/79b7cab50a3292a1c014
- version: 3.14.0a2+
- config: NOGIL
- commit hash: [79b7cab](https://github.com/python/cpython/commit/79b7cab)
- commit date: 2024-12-07T17:58:42+00:00
- commit merge base: [27d0d2141319d82709eb09ba20065df3e1714fab](https://github.com/python/cpython/commit/27d0d2141319d82709eb09ba20065df3e1714fab)
- ref: 79b7cab50a3292a1c014

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.105x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.56x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.293x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.287x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.308x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.067x faster (HPT: reliability of 99.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.176x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.222x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.242x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms, mypy2
- [🧠memory plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-linux-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.006x slower (HPT: reliability of 56.45%, 1.00x slower at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.227x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.212x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.239x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-pythonperf2-x86_64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12217123974)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab.json)

### vs. 3.10.4

- Geometric mean: 1.020x faster (HPT: reliability of 54.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x slower (HPT: reliability of 99.90%, 1.03x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.116x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.186x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.14x
- [🧠memory plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base-mem.svg)
- [📄table](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.md)
- [📈time plot](bm-20241207-darwin-arm64-python-79b7cab50a3292a1c014-3.14.0a2%2B-79b7cab-vs-base.svg)

