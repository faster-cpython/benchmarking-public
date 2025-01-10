# Results

- fork: python/7dc41ad6a7826ffc675f
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [7dc41ad](https://github.com/python/cpython/commit/7dc41ad)
- commit date: 2025-01-09T21:26:00+05:30
- commit merge base: [b725297cee9e5608b709f3c7291d974c97f68fff](https://github.com/python/cpython/commit/b725297cee9e5608b709f3c7291d974c97f68fff)
- ref: 7dc41ad6a7826ffc675f

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696200281)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad.json)

### vs. 3.10.4

- Geometric mean: 1.140x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-3.10.4.md)
- [📈time plot](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-3.12.0.md)
- [📈time plot](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.169x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-3.13.0.md)
- [📈time plot](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.204x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.18x
- [🧠memory plot](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-base-mem.svg)
- [📄table](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-base.md)
- [📈time plot](bm-20250109-linux-x86_64-python-7dc41ad6a7826ffc675f-3.14.0a3%2B-7dc41ad-vs-base.svg)

