# Results

- fork: python/48d0d0dd9733eae4935f
- version: 3.15.0a0
- config: JIT
- commit hash: [48d0d0d](https://github.com/python/cpython/commit/48d0d0d)
- commit date: 2025-09-26T19:44:36-07:00
- commit merge base: [93ac3525b92f5f8918211a241c01324dfa8b1e5e](https://github.com/python/cpython/commit/93ac3525b92f5f8918211a241c01324dfa8b1e5e)
- ref: 48d0d0dd9733eae4935f

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18066558438)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json)

### vs. 3.10.4

- Geometric mean: 1.342x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.10.4.md)
- [📈time plot](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.12.0.md)
- [📈time plot](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.13.0.md)
- [📈time plot](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 99.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-base-mem.svg)
- [📄table](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-base.md)
- [📈time plot](bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18066558438)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json)

### vs. 3.10.4

- Geometric mean: 1.351x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.10.4.md)
- [📈time plot](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.153x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.12.0.md)
- [📈time plot](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.104x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.13.0.md)
- [📈time plot](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.029x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-base.md)
- [📈time plot](bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18066558438)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json)

### vs. 3.10.4

- Geometric mean: 1.516x faster (HPT: reliability of 100.00%, 1.42x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.10.4.md)
- [📈time plot](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.537x faster (HPT: reliability of 100.00%, 1.48x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.12.0.md)
- [📈time plot](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.323x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.13.0.md)
- [📈time plot](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.052x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-base.md)
- [📈time plot](bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d-vs-base.svg)

