# Results

- fork: python/94b8f8b40943bf38cf5c
- version: 3.14.0a2+
- config: JIT
- commit hash: [94b8f8b](https://github.com/python/cpython/commit/94b8f8b)
- commit date: 2024-12-04T15:01:28-08:00
- commit merge base: [7c5a6f67c726608a05a640e76fc62cfbae986a03](https://github.com/python/cpython/commit/7c5a6f67c726608a05a640e76fc62cfbae986a03)
- ref: 94b8f8b40943bf38cf5c

## linux x86_64 (azure)

- [pystats raw](bm-20241204-azure-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-pystats.json)
- [pystats table](bm-20241204-azure-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12263122434)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b.json)

### vs. 3.10.4

- Geometric mean: 1.438x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-vs-3.10.4.md)
- [📈time plot](bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-vs-3.12.0.md)
- [📈time plot](bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.05%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-vs-3.13.0.md)
- [📈time plot](bm-20241204-linux-x86_64-python-94b8f8b40943bf38cf5c-3.14.0a2%2B-94b8f8b-vs-3.13.0.svg)

