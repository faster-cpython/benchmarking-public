# Results

- fork: python
- version: 3.14.0a1+
- config: NOGIL
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

- Geometric mean: 1.204x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.370x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.375x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.362x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.045x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.49x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.260x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.296x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.299x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-linux-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.095x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.294x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.286x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.296x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11760425481)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423.json)

### vs. 3.10.4

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.49x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.229x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.211x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.239x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.13x
- [🧠memory plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base-mem.svg)
- [📄table](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.md)
- [📈time plot](bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1%2B-9d08423-vs-base.svg)

