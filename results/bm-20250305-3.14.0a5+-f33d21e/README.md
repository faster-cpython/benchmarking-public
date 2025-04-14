# Results

- fork: python/f33d21e24fdb05da7512
- version: 3.14.0a5+
- config: 
- commit hash: [f33d21e](https://github.com/python/cpython/commit/f33d21e)
- commit date: 2025-03-05T13:10:05+02:00
- commit merge base: [67a942d4272145ccdbdf4ceff31318e176f71355](https://github.com/python/cpython/commit/67a942d4272145ccdbdf4ceff31318e176f71355)
- ref: f33d21e24fdb05da7512

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13677223824)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5%2B-f33d21e.json)

### vs. 3.10.4

- Geometric mean: 1.212x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5%2B-f33d21e-vs-3.10.4.md)
- [📈time plot](bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5%2B-f33d21e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x faster (HPT: reliability of 88.51%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5%2B-f33d21e-vs-3.12.0.md)
- [📈time plot](bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5%2B-f33d21e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5%2B-f33d21e-vs-3.13.0.md)
- [📈time plot](bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5%2B-f33d21e-vs-3.13.0.svg)

