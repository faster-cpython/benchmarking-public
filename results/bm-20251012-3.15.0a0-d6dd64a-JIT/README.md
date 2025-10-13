# Results

- fork: python/d6dd64ac654898b4ce71
- version: 3.15.0a0
- config: JIT
- commit hash: [d6dd64a](https://github.com/python/cpython/commit/d6dd64a)
- commit date: 2025-10-12T01:52:01+03:00
- commit merge base: [35e9d41a9cc3999672ba7440847b16ec71bd9ddd](https://github.com/python/cpython/commit/35e9d41a9cc3999672ba7440847b16ec71bd9ddd)
- ref: d6dd64ac654898b4ce71

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18436369837)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.10.4.md)
- [📈time plot](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.12.0.md)
- [📈time plot](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.13.0.md)
- [📈time plot](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 52.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-base-mem.svg)
- [📄table](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-base.md)
- [📈time plot](bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18436369837)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json)

### vs. 3.10.4

- Geometric mean: 1.362x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.10.4.md)
- [📈time plot](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.163x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.12.0.md)
- [📈time plot](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.113x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.13.0.md)
- [📈time plot](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.048x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-base.md)
- [📈time plot](bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18436369837)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json)

### vs. 3.10.4

- Geometric mean: 1.521x faster (HPT: reliability of 100.00%, 1.42x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.10.4.md)
- [📈time plot](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.543x faster (HPT: reliability of 100.00%, 1.49x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.12.0.md)
- [📈time plot](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.13.0.md)
- [📈time plot](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-base.md)
- [📈time plot](bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a-vs-base.svg)

