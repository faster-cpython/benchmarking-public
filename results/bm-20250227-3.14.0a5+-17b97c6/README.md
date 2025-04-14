# Results

- fork: faster-cpython/use_stackref_macros
- version: 3.14.0a5+
- config: 
- commit hash: [17b97c6](https://github.com/faster%2dcpython/cpython/commit/17b97c6)
- commit date: 2025-02-27T12:31:30+00:00
- commit merge base: [014223649c33b2febbccfa221c2ab7f18a8c0847](https://github.com/python/cpython/commit/014223649c33b2febbccfa221c2ab7f18a8c0847)
- ref: use_stackref_macros

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13566467416)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6.json)

### vs. 3.10.4

- Geometric mean: 1.218x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-3.10.4.md)
- [📈time plot](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 75.75%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-3.12.0.md)
- [📈time plot](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-3.13.0.md)
- [📈time plot](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.017x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-base.md)
- [📈time plot](bm-20250227-pythonperf1-amd64-faster%252dcpython-use_stackref_macros-3.14.0a5%2B-17b97c6-vs-base.svg)

