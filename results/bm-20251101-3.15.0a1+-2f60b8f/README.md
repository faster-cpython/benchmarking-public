# Results

- fork: python/2f60b8f02fe7cb83dd58
- version: 3.15.0a1+
- config: 
- commit hash: [2f60b8f](https://github.com/python/cpython/commit/2f60b8f)
- commit date: 2025-11-01T16:41:23+00:00
- commit merge base: [b1554146c29182803d1df23d6367c07a429d21ba](https://github.com/python/cpython/commit/b1554146c29182803d1df23d6367c07a429d21ba)
- ref: 2f60b8f02fe7cb83dd58

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/19004509735)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f.json)

### vs. 3.10.4

- Geometric mean: 1.359x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.39x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.10.4.md)
- [📈time plot](bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.12.0.md)
- [📈time plot](bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.13.0.md)
- [📈time plot](bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/19004509735)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f.json)

### vs. 3.10.4

- Geometric mean: 1.287x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.10.4.md)
- [📈time plot](bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.12.0.md)
- [📈time plot](bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 91.81%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.13.0.md)
- [📈time plot](bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.13.0.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/19004509735)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f.json)

### vs. 3.10.4

- Geometric mean: 1.467x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.10.4.md)
- [📈time plot](bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.490x faster (HPT: reliability of 100.00%, 1.44x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.12.0.md)
- [📈time plot](bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.288x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.13.0.md)
- [📈time plot](bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1%2B-2f60b8f-vs-3.13.0.svg)

