# Results

- fork: python/20d5494c88985beb925b
- version: 3.15.0a0
- config: JIT
- commit hash: [20d5494](https://github.com/python/cpython/commit/20d5494)
- commit date: 2025-09-20T11:01:44+03:00
- commit merge base: [69c6b438e84ef2bb94a587e49946a2a4b6454fb3](https://github.com/python/cpython/commit/69c6b438e84ef2bb94a587e49946a2a4b6454fb3)
- ref: 20d5494c88985beb925b

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17886382718)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.10.4.md)
- [📈time plot](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.12.0.md)
- [📈time plot](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.13.0.md)
- [📈time plot](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 91.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-base-mem.svg)
- [📄table](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-base.md)
- [📈time plot](bm-20250920-pythonperf2-x86_64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17886382718)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json)

### vs. 3.10.4

- Geometric mean: 1.323x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.10.4.md)
- [📈time plot](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.131x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.12.0.md)
- [📈time plot](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.082x faster (HPT: reliability of 87.52%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.13.0.md)
- [📈time plot](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.031x faster (HPT: reliability of 93.27%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-base.md)
- [📈time plot](bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17886382718)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json)

### vs. 3.10.4

- Geometric mean: 1.490x faster (HPT: reliability of 100.00%, 1.39x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.10.4.md)
- [📈time plot](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.511x faster (HPT: reliability of 100.00%, 1.45x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.12.0.md)
- [📈time plot](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.301x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.13.0.md)
- [📈time plot](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.039x faster (HPT: reliability of 96.06%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-base.md)
- [📈time plot](bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494-vs-base.svg)

