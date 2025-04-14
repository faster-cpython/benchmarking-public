# Results

- fork: python/5ab9604683a58e613c6e
- version: 3.14.0a4+
- config: 
- commit hash: [5ab9604](https://github.com/python/cpython/commit/5ab9604)
- commit date: 2025-01-30T11:38:52+00:00
- commit merge base: [a810cb89f108f026d70c5b20141b709493051d96](https://github.com/python/cpython/commit/a810cb89f108f026d70c5b20141b709493051d96)
- ref: 5ab9604683a58e613c6e

## linux x86_64 (azure)

- [pystats raw](bm-20250130-azure-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-pystats.json)
- [pystats table](bm-20250130-azure-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13125128215)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604.json)

### vs. 3.10.4

- Geometric mean: 1.445x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-vs-3.10.4.md)
- [📈time plot](bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-vs-3.12.0.md)
- [📈time plot](bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-vs-3.13.0.md)
- [📈time plot](bm-20250130-linux-x86_64-python-5ab9604683a58e613c6e-3.14.0a4%2B-5ab9604-vs-3.13.0.svg)

