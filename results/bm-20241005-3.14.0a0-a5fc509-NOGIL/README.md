# Results

- fork: python/a5fc50994a3fae46d0c3
- version: 3.14.0a0
- config: NOGIL
- commit hash: [a5fc509](https://github.com/python/cpython/commit/a5fc509)
- commit date: 2024-10-05T11:27:32+09:00
- commit merge base: [adfe7657a3f1ce5d8384694ed27a40376a18fa6c](https://github.com/python/cpython/commit/adfe7657a3f1ce5d8384694ed27a40376a18fa6c)
- ref: a5fc50994a3fae46d0c3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11213229021)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509.json)

### vs. 3.10.4

- Geometric mean: 1.028x slower (HPT: reliability of 99.54%, 1.01x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509-vs-3.10.4.md)
- [📈time plot](bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.249x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509-vs-3.12.0.md)
- [📈time plot](bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.290x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509-vs-3.13.0.md)
- [📈time plot](bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509-vs-3.13.0.svg)

