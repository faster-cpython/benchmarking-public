# Results

- fork: python/2228e92da31ca7344a16
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [2228e92](https://github.com/python/cpython/commit/2228e92)
- commit date: 2025-01-05T12:07:18+00:00
- commit merge base: [ae23a012e6c8aadc4a588101cbe7bc86ede45627](https://github.com/python/cpython/commit/ae23a012e6c8aadc4a588101cbe7bc86ede45627)
- ref: 2228e92da31ca7344a16

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.059x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.254x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.248x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.271x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base-mem.svg)
- [📄table](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.120x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.132x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.180x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.211x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.18x
- [🧠memory plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base-mem.svg)
- [📄table](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.050x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.180x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.163x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.210x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base-mem.svg)
- [📄table](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92.json)

### vs. 3.10.4

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x slower (HPT: reliability of 99.57%, 1.01x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x slower (HPT: reliability of 99.81%, 1.01x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.171x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.13x
- [🧠memory plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base-mem.svg)
- [📄table](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.md)
- [📈time plot](bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3%2B-2228e92-vs-base.svg)

