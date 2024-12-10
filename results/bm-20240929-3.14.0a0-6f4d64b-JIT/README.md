# Results

- fork: python/6f4d64b048133c60d407
- version: 3.14.0a0
- config: JIT
- commit hash: [6f4d64b](https://github.com/python/cpython/commit/6f4d64b)
- commit date: 2024-09-29T20:47:45-05:00
- commit merge base: [b5774603a0c877f19b33fb922e2fb967b1d50329](https://github.com/python/cpython/commit/b5774603a0c877f19b33fb922e2fb967b1d50329)
- ref: 6f4d64b048133c60d407

## linux x86_64 (azure)

- [pystats raw](bm-20240929-azure-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-pystats.json)
- [pystats table](bm-20240929-azure-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11134116722)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b.json)

### vs. 3.10.4

- Geometric mean: 1.418x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.10.4.md)
- [📈time plot](bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.12.0.md)
- [📈time plot](bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 83.89%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.13.0.md)
- [📈time plot](bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b-vs-3.13.0.svg)

