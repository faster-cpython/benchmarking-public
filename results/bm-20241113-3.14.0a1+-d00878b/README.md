# Results

- fork: python/d00878b06a05ea047908
- version: 3.14.0a1+
- config: 
- commit hash: [d00878b](https://github.com/python/cpython/commit/d00878b)
- commit date: 2024-11-13T13:27:16+00:00
- commit merge base: [29b5323c4567dc7772e1d30a7ba1cbad52fe10a9](https://github.com/python/cpython/commit/29b5323c4567dc7772e1d30a7ba1cbad52fe10a9)
- ref: d00878b06a05ea047908

## linux x86_64 (azure)

- [pystats raw](bm-20241113-azure-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-pystats.json)
- [pystats table](bm-20241113-azure-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11986259378)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241113-linux-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b.json)

### vs. 3.10.4

- Geometric mean: 1.401x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241113-linux-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-vs-3.10.4.md)
- [📈time plot](bm-20241113-linux-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241113-linux-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-vs-3.12.0.md)
- [📈time plot](bm-20241113-linux-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 67.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241113-linux-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-vs-3.13.0.md)
- [📈time plot](bm-20241113-linux-x86_64-python-d00878b06a05ea047908-3.14.0a1%2B-d00878b-vs-3.13.0.svg)

