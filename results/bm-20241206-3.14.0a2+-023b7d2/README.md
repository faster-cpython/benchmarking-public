# Results

- fork: python/023b7d2141467017abc2
- version: 3.14.0a2+
- config: 
- commit hash: [023b7d2](https://github.com/python/cpython/commit/023b7d2)
- commit date: 2024-12-06T10:46:59+00:00
- commit merge base: [8b7c194c7bf7e547e4f6317528f0dcb9344c18c7](https://github.com/python/cpython/commit/8b7c194c7bf7e547e4f6317528f0dcb9344c18c7)
- ref: 023b7d2141467017abc2

## linux x86_64 (azure)

- [pystats raw](bm-20241206-azure-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-pystats.json)
- [pystats table](bm-20241206-azure-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12198100366)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-vs-3.10.4.md)
- [📈time plot](bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-vs-3.12.0.md)
- [📈time plot](bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 99.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-vs-3.13.0.md)
- [📈time plot](bm-20241206-linux-x86_64-python-023b7d2141467017abc2-3.14.0a2%2B-023b7d2-vs-3.13.0.svg)

