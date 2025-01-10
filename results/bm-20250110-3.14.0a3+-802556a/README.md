# Results

- fork: python/802556abfa008abe0bdd
- version: 3.14.0a3+
- config: 
- commit hash: [802556a](https://github.com/python/cpython/commit/802556a)
- commit date: 2025-01-10T13:59:51+01:00
- commit merge base: [688f3a0d4b94874ff6d72af3baafd8bbf911153e](https://github.com/python/cpython/commit/688f3a0d4b94874ff6d72af3baafd8bbf911153e)
- ref: 802556abfa008abe0bdd

## linux x86_64 (azure)

- [pystats raw](bm-20250110-azure-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-pystats.json)
- [pystats table](bm-20250110-azure-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12713990641)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a.json)

### vs. 3.10.4

- Geometric mean: 1.439x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-vs-3.10.4.md)
- [📈time plot](bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-vs-3.12.0.md)
- [📈time plot](bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-vs-3.13.0.md)
- [📈time plot](bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3%2B-802556a-vs-3.13.0.svg)

