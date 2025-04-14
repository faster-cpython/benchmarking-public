# Results

- fork: python/555dc50c811e3e9ebdc3
- version: 3.14.0a4+
- config: 
- commit hash: [555dc50](https://github.com/python/cpython/commit/555dc50)
- commit date: 2025-02-06T15:19:00+00:00
- commit merge base: [55f17b77c305be877ac856d6426b13591cbc7fc8](https://github.com/python/cpython/commit/55f17b77c305be877ac856d6426b13591cbc7fc8)
- ref: 555dc50c811e3e9ebdc3

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13199468698)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4%2B-555dc50.json)

### vs. 3.10.4

- Geometric mean: 1.231x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4%2B-555dc50-vs-3.10.4.md)
- [📈time plot](bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4%2B-555dc50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 73.97%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4%2B-555dc50-vs-3.12.0.md)
- [📈time plot](bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4%2B-555dc50-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4%2B-555dc50-vs-3.13.0.md)
- [📈time plot](bm-20250206-pythonperf1-amd64-python-555dc50c811e3e9ebdc3-3.14.0a4%2B-555dc50-vs-3.13.0.svg)

