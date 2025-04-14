# Results

- fork: python/3829104ab412a47bf3f3
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [3829104](https://github.com/python/cpython/commit/3829104)
- commit date: 2025-01-17T16:49:16-08:00
- commit merge base: [8174770d311ba09c07a47cc3ae90a1db2e7d7708](https://github.com/python/cpython/commit/8174770d311ba09c07a47cc3ae90a1db2e7d7708)
- ref: 3829104ab412a47bf3f3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104.json)

### vs. 3.10.4

- Geometric mean: 1.090x faster (HPT: reliability of 99.52%, 1.00x faster at 99th %ile)
- Memory usage: 1.57x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.md)
- [📈time plot](bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.132x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.md)
- [📈time plot](bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.135x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.md)
- [📈time plot](bm-20250117-arminc-aarch64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250117-linux-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104.json)

### vs. 3.10.4

- Geometric mean: 1.241x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250117-linux-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.md)
- [📈time plot](bm-20250117-linux-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x slower (HPT: reliability of 99.95%, 1.02x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250117-linux-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.md)
- [📈time plot](bm-20250117-linux-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-linux-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.md)
- [📈time plot](bm-20250117-linux-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.md)
- [📈time plot](bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.075x slower (HPT: reliability of 99.98%, 1.05x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.md)
- [📈time plot](bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x slower (HPT: reliability of 99.97%, 1.02x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.md)
- [📈time plot](bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939809594)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104.json)

### vs. 3.10.4

- Geometric mean: 1.295x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.md)
- [📈time plot](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 63.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.md)
- [📈time plot](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 98.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.md)
- [📈time plot](bm-20250117-darwin-arm64-python-3829104ab412a47bf3f3-3.14.0a4%2B-3829104-vs-3.13.0.svg)

