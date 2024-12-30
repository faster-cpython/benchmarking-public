# Results

- fork: python/f9a5a3a3ef34e63dc197
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [f9a5a3a](https://github.com/python/cpython/commit/f9a5a3a)
- commit date: 2024-12-28T21:05:34+00:00
- commit merge base: [492b224b991cd9027f1bc6d9988d01e94f764992](https://github.com/python/cpython/commit/492b224b991cd9027f1bc6d9988d01e94f764992)
- ref: f9a5a3a3ef34e63dc197

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.068x slower (HPT: reliability of 99.98%, 1.04x slower at 99th %ile)
- Memory usage: 1.54x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.260x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.254x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.278x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base-mem.svg)
- [📄table](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.133x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.181x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.208x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base-mem.svg)
- [📄table](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-linux-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12530739237)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a.json)

### vs. 3.10.4

- Geometric mean: 1.048x faster (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.182x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.166x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.213x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base-mem.svg)
- [📄table](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.md)
- [📈time plot](bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3%2B-f9a5a3a-vs-base.svg)

