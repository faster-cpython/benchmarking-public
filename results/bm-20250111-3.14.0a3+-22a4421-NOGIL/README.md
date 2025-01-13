# Results

- fork: python/22a442181d5f1ac496da
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [22a4421](https://github.com/python/cpython/commit/22a4421)
- commit date: 2025-01-11T19:27:47+00:00
- commit merge base: [0946ed25b53dddfa4eb040513720353b7214d71b](https://github.com/python/cpython/commit/0946ed25b53dddfa4eb040513720353b7214d71b)
- ref: 22a442181d5f1ac496da

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.043x slower (HPT: reliability of 99.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.56x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.242x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.238x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.268x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base-mem.svg)
- [📄table](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.md)
- [📈time plot](bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.129x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.127x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.177x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.212x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base-mem.svg)
- [📄table](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.md)
- [📈time plot](bm-20250111-linux-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.171x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.158x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.205x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base-mem.svg)
- [📄table](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.md)
- [📈time plot](bm-20250111-pythonperf2-x86_64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12728647995)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421.json)

### vs. 3.10.4

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.md)
- [📈time plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.074x slower (HPT: reliability of 98.13%, 1.00x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.md)
- [📈time plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x slower (HPT: reliability of 99.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.md)
- [📈time plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.162x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.13x
- [🧠memory plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base-mem.svg)
- [📄table](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.md)
- [📈time plot](bm-20250111-darwin-arm64-python-22a442181d5f1ac496da-3.14.0a3%2B-22a4421-vs-base.svg)

