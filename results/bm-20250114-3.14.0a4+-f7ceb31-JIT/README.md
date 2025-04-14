# Results

- fork: python/f7ceb317aec498823555
- version: 3.14.0a4+
- config: JIT
- commit hash: [f7ceb31](https://github.com/python/cpython/commit/f7ceb31)
- commit date: 2025-01-14T22:40:45+02:00
- commit merge base: [b5ee0258bf5bb60a5a5a65c64717853e06b64808](https://github.com/python/cpython/commit/b5ee0258bf5bb60a5a5a65c64717853e06b64808)
- ref: f7ceb317aec498823555

## linux x86_64 (azure)

- [pystats raw](bm-20250114-azure-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-pystats.json)
- [pystats table](bm-20250114-azure-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12778665544)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-vs-3.10.4.md)
- [📈time plot](bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-vs-3.12.0.md)
- [📈time plot](bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 98.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-vs-3.13.0.md)
- [📈time plot](bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4%2B-f7ceb31-vs-3.13.0.svg)

