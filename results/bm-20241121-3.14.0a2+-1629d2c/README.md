# Results

- fork: python/1629d2ca56014beb2d46
- version: 3.14.0a2+
- config: 
- commit hash: [1629d2c](https://github.com/python/cpython/commit/1629d2c)
- commit date: 2024-11-21T15:10:46+11:00
- commit merge base: [32428cf9ea03bce6d64c7acd28e0b7d92774eb53](https://github.com/python/cpython/commit/32428cf9ea03bce6d64c7acd28e0b7d92774eb53)
- ref: 1629d2ca56014beb2d46

## linux x86_64 (azure)

- [pystats raw](bm-20241121-azure-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-pystats.json)
- [pystats table](bm-20241121-azure-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11974349921)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c.json)

### vs. 3.10.4

- Geometric mean: 1.395x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-vs-3.10.4.md)
- [📈time plot](bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-vs-3.12.0.md)
- [📈time plot](bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 64.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-vs-3.13.0.md)
- [📈time plot](bm-20241121-linux-x86_64-python-1629d2ca56014beb2d46-3.14.0a2%2B-1629d2c-vs-3.13.0.svg)

