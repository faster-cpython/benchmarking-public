# Results

- fork: mdboom/test_without_pgo_wor
- version: 3.14.0a4+
- config: 
- commit hash: [71a13ea](https://github.com/mdboom/cpython/commit/71a13ea)
- commit date: 2025-01-23T12:56:42-05:00
- commit merge base: [f18b2264929c56360c868d7ad77508035d751352](https://github.com/python/cpython/commit/f18b2264929c56360c868d7ad77508035d751352)
- ref: test_without_pgo_wor

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12939226379)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea.json)

### vs. 3.10.4

- Geometric mean: 1.164x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.10.4.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x slower (HPT: reliability of 99.31%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.12.0.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.13.0.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 96.38%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-base.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-base.svg)

