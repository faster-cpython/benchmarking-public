# Results

- fork: python
- version: 3.14.0a1+
- config: 
- commit hash: [bfc1d25](https://github.com/python/cpython/commit/bfc1d25)
- commit date: 2024-11-04T13:15:57+03:00
- commit merge base: [fe5a6ab7bea927e887b7b3c2d4e8fe8eac7106c3](https://github.com/python/cpython/commit/fe5a6ab7bea927e887b7b3c2d4e8fe8eac7106c3)
- ref: bfc1d2504c183a9464e6

## linux x86_64 (azure)

- [pystats raw](bm-20241104-azure-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-pystats.json)
- [pystats table](bm-20241104-azure-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11664284848)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25.json)

### vs. 3.10.4

- Geometric mean: 1.405x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-vs-3.10.4.md)
- [📈time plot](bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-vs-3.12.0.md)
- [📈time plot](bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 75.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-vs-3.13.0.md)
- [📈time plot](bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1%2B-bfc1d25-vs-3.13.0.svg)

