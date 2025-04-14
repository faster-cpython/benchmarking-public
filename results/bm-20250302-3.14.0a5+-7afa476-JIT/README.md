# Results

- fork: python/7afa476874b9a432ad6d
- version: 3.14.0a5+
- config: JIT
- commit hash: [7afa476](https://github.com/python/cpython/commit/7afa476)
- commit date: 2025-03-02T13:21:34-08:00
- commit merge base: [c6513f7a627c8918a5e3f3733fa47d34a94ddff9](https://github.com/python/cpython/commit/c6513f7a627c8918a5e3f3733fa47d34a94ddff9)
- ref: 7afa476874b9a432ad6d

## linux x86_64 (azure)

- [pystats raw](bm-20250302-azure-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-pystats.json)
- [pystats table](bm-20250302-azure-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13647470332)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476.json)

### vs. 3.10.4

- Geometric mean: 1.442x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-vs-3.10.4.md)
- [📈time plot](bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-vs-3.12.0.md)
- [📈time plot](bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-vs-3.13.0.md)
- [📈time plot](bm-20250302-linux-x86_64-python-7afa476874b9a432ad6d-3.14.0a5%2B-7afa476-vs-3.13.0.svg)

