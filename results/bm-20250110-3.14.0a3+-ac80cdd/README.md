# Results

- fork: Fidget-Spinner/tail_call
- version: 3.14.0a3+
- config: 
- commit hash: [ac80cdd](https://github.com/Fidget%2dSpinner/cpython/commit/ac80cdd)
- commit date: 2025-01-10T22:47:55+08:00
- commit merge base: [2228e92da31ca7344a163498f848973a1b356597](https://github.com/python/cpython/commit/2228e92da31ca7344a163498f848973a1b356597)
- ref: tail_call

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12712222122)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd.json)

### vs. 3.10.4

- Geometric mean: 1.167x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-3.10.4.md)
- [📈time plot](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 99.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-3.12.0.md)
- [📈time plot](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-3.13.0.md)
- [📈time plot](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-base.md)
- [📈time plot](bm-20250110-pythonperf1-amd64-Fidget%252dSpinner-tail_call-3.14.0a3%2B-ac80cdd-vs-base.svg)

