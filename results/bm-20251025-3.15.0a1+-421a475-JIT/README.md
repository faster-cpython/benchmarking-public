# Results

- fork: python/421a475c87771d46752c
- version: 3.15.0a1+
- config: JIT
- commit hash: [421a475](https://github.com/python/cpython/commit/421a475)
- commit date: 2025-10-25T18:29:46-05:00
- commit merge base: [d74a96366df58b6e55d4a03612c3e67da2211ddd](https://github.com/python/cpython/commit/d74a96366df58b6e55d4a03612c3e67da2211ddd)
- ref: 421a475c87771d46752c

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18810184550)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475.json)

### vs. 3.10.4

- Geometric mean: 1.352x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.10.4.md)
- [📈time plot](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.12.0.md)
- [📈time plot](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.13.0.md)
- [📈time plot](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 51.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-base-mem.svg)
- [📄table](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-base.md)
- [📈time plot](bm-20251025-pythonperf2-x86_64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18810184550)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475.json)

### vs. 3.10.4

- Geometric mean: 1.370x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.10.4.md)
- [📈time plot](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.172x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.12.0.md)
- [📈time plot](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.13.0.md)
- [📈time plot](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.032x faster (HPT: reliability of 98.15%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-base.md)
- [📈time plot](bm-20251025-pythonperf1-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18810184550)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475.json)

### vs. 3.10.4

- Geometric mean: 1.510x faster (HPT: reliability of 100.00%, 1.41x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.10.4.md)
- [📈time plot](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.536x faster (HPT: reliability of 100.00%, 1.47x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.12.0.md)
- [📈time plot](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.324x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.13.0.md)
- [📈time plot](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.027x faster (HPT: reliability of 97.56%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-base.md)
- [📈time plot](bm-20251025-pythonperf1_win32-amd64-python-421a475c87771d46752c-3.15.0a1%2B-421a475-vs-base.svg)

