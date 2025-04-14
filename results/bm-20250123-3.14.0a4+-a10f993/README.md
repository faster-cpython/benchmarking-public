# Results

- fork: python/a10f99375e7912df863c
- version: 3.14.0a4+
- config: 
- commit hash: [a10f993](https://github.com/python/cpython/commit/a10f993)
- commit date: 2025-01-23T09:26:25+00:00
- commit merge base: [d7d066c3ab6842117f9e0fb1c9dde4bce00fa1e3](https://github.com/python/cpython/commit/d7d066c3ab6842117f9e0fb1c9dde4bce00fa1e3)
- ref: a10f99375e7912df863c

## linux x86_64 (azure)

- [pystats raw](bm-20250123-azure-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-pystats.json)
- [pystats table](bm-20250123-azure-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12931778503)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993.json)

### vs. 3.10.4

- Geometric mean: 1.361x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-vs-3.10.4.md)
- [📈time plot](bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-vs-3.12.0.md)
- [📈time plot](bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-vs-3.13.0.md)
- [📈time plot](bm-20250123-pythonperf2-x86_64-python-a10f99375e7912df863c-3.14.0a4%2B-a10f993-vs-3.13.0.svg)

