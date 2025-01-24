# Results

- fork: python/7907203bc07387ff2d8e
- version: 3.14.0a4+
- config: JIT
- commit hash: [7907203](https://github.com/python/cpython/commit/7907203)
- commit date: 2025-01-24T18:33:40+02:00
- commit merge base: [8e0b36006c0b82e47e1cb5d367ec78532f21cee5](https://github.com/python/cpython/commit/8e0b36006c0b82e47e1cb5d367ec78532f21cee5)
- ref: 7907203bc07387ff2d8e

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12955147896)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4%2B-7907203.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.70x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4%2B-7907203-vs-3.10.4.md)
- [📈time plot](bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4%2B-7907203-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4%2B-7907203-vs-3.12.0.md)
- [📈time plot](bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4%2B-7907203-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 98.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4%2B-7907203-vs-3.13.0.md)
- [📈time plot](bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4%2B-7907203-vs-3.13.0.svg)

