# Results

- fork: python/94cd2e0ddeff83dee325
- version: 3.14.0a4+
- config: 
- commit hash: [94cd2e0](https://github.com/python/cpython/commit/94cd2e0)
- commit date: 2025-02-10T17:03:59+05:30
- commit merge base: [7c156a63d3d5aadff0d40af73c0f622f7a0fcea5](https://github.com/python/cpython/commit/7c156a63d3d5aadff0d40af73c0f622f7a0fcea5)
- ref: 94cd2e0ddeff83dee325

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13243608391)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4%2B-94cd2e0.json)

### vs. 3.10.4

- Geometric mean: 1.456x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4%2B-94cd2e0-vs-3.10.4.md)
- [📈time plot](bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4%2B-94cd2e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4%2B-94cd2e0-vs-3.12.0.md)
- [📈time plot](bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4%2B-94cd2e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4%2B-94cd2e0-vs-3.13.0.md)
- [📈time plot](bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4%2B-94cd2e0-vs-3.13.0.svg)

