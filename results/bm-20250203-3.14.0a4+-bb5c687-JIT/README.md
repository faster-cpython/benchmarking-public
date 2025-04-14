# Results

- fork: python/bb5c6875d6e84bf2b4e1
- version: 3.14.0a4+
- config: JIT
- commit hash: [bb5c687](https://github.com/python/cpython/commit/bb5c687)
- commit date: 2025-02-03T16:42:12+00:00
- commit merge base: [75b628adebd4594529da25ea9915600f2872fc2b](https://github.com/python/cpython/commit/75b628adebd4594529da25ea9915600f2872fc2b)
- ref: bb5c6875d6e84bf2b4e1

## linux x86_64 (azure)

- [pystats raw](bm-20250203-azure-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-pystats.json)
- [pystats table](bm-20250203-azure-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13124151404)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-vs-3.10.4.md)
- [📈time plot](bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-vs-3.12.0.md)
- [📈time plot](bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-vs-3.13.0.md)
- [📈time plot](bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4%2B-bb5c687-vs-3.13.0.svg)

