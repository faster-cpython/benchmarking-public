# Results

- fork: python/014223649c33b2febbcc
- version: 3.14.0a5+
- config: 
- commit hash: [0142236](https://github.com/python/cpython/commit/0142236)
- commit date: 2025-02-25T09:24:48+00:00
- commit merge base: [99088ab081279329b8362e1c24533fa0be303e6f](https://github.com/python/cpython/commit/99088ab081279329b8362e1c24533fa0be303e6f)
- ref: 014223649c33b2febbcc

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13518789509)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5%2B-0142236.json)

### vs. 3.10.4

- Geometric mean: 1.239x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5%2B-0142236-vs-3.10.4.md)
- [📈time plot](bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5%2B-0142236-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x faster (HPT: reliability of 69.69%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5%2B-0142236-vs-3.12.0.md)
- [📈time plot](bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5%2B-0142236-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x faster (HPT: reliability of 99.89%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5%2B-0142236-vs-3.13.0.md)
- [📈time plot](bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5%2B-0142236-vs-3.13.0.svg)

