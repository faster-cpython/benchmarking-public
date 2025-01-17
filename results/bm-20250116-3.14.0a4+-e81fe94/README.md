# Results

- fork: python/e81fe940c9bd092f6de5
- version: 3.14.0a4+
- config: 
- commit hash: [e81fe94](https://github.com/python/cpython/commit/e81fe94)
- commit date: 2025-01-16T13:15:52+00:00
- commit merge base: [3193cb5ef87b77158d5c9bef99ae445cb82727de](https://github.com/python/cpython/commit/3193cb5ef87b77158d5c9bef99ae445cb82727de)
- ref: e81fe940c9bd092f6de5

## linux x86_64 (azure)

- [pystats raw](bm-20250116-azure-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-pystats.json)
- [pystats table](bm-20250116-azure-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12818232467)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94.json)

### vs. 3.10.4

- Geometric mean: 1.444x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.10.4.md)
- [📈time plot](bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.12.0.md)
- [📈time plot](bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.13.0.md)
- [📈time plot](bm-20250116-linux-x86_64-python-e81fe940c9bd092f6de5-3.14.0a4%2B-e81fe94-vs-3.13.0.svg)

