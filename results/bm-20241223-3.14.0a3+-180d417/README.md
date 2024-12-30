# Results

- fork: python/180d417e9f9456defd4c
- version: 3.14.0a3+
- config: 
- commit hash: [180d417](https://github.com/python/cpython/commit/180d417)
- commit date: 2024-12-23T13:31:33+01:00
- commit merge base: [831b6de6d725c697f2f61fd35c4448cd8a9354ff](https://github.com/python/cpython/commit/831b6de6d725c697f2f61fd35c4448cd8a9354ff)
- ref: 180d417e9f9456defd4c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12549470888)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417.json)

### vs. 3.10.4

- Geometric mean: 1.428x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.10.4.md)
- [📈time plot](bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.12.0.md)
- [📈time plot](bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.13.0.md)
- [📈time plot](bm-20241223-linux-x86_64-python-180d417e9f9456defd4c-3.14.0a3%2B-180d417-vs-3.13.0.svg)

