# Results

- fork: python/0cafa97932c6574734bb
- version: 3.14.0a3+
- config: CLANG
- commit hash: [0cafa97](https://github.com/python/cpython/commit/0cafa97)
- commit date: 2025-01-04T23:38:46+00:00
- commit merge base: [e8b6b39ff707378da654e15ccddde9c28cefdd30](https://github.com/python/cpython/commit/e8b6b39ff707378da654e15ccddde9c28cefdd30)
- ref: 0cafa97932c6574734bb

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696216516)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97.json)

### vs. 3.10.4

- Geometric mean: 1.167x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x slower (HPT: reliability of 99.29%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.032x slower (HPT: reliability of 99.58%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 mypy2
- [📄table](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.md)
- [📈time plot](bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3%2B-0cafa97-vs-base.svg)

