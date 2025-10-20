# Results

- fork: python/bedaea05987738c4c6b9
- version: 3.15.0a1+
- config: NOGIL
- commit hash: [bedaea0](https://github.com/python/cpython/commit/bedaea0)
- commit date: 2025-10-19T00:20:04+01:00
- commit merge base: [920de7ccdcfa7284b6d23a124771b17c66dd3e4f](https://github.com/python/cpython/commit/920de7ccdcfa7284b6d23a124771b17c66dd3e4f)
- ref: bedaea05987738c4c6b9

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18622655866)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0.json)

### vs. 3.10.4

- Geometric mean: 1.213x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.69x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.10.4.md)
- [📈time plot](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x slower (HPT: reliability of 95.03%, 1.00x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.12.0.md)
- [📈time plot](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 89.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.13.0.md)
- [📈time plot](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-base-mem.svg)
- [📄table](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-base.md)
- [📈time plot](bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18622655866)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0.json)

### vs. 3.10.4

- Geometric mean: 1.185x faster (HPT: reliability of 99.99%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.10.4.md)
- [📈time plot](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 95.01%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.12.0.md)
- [📈time plot](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x slower (HPT: reliability of 99.94%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.13.0.md)
- [📈time plot](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.107x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-base.md)
- [📈time plot](bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18622655866)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0.json)

### vs. 3.10.4

- Geometric mean: 1.340x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.10.4.md)
- [📈time plot](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.374x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.12.0.md)
- [📈time plot](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.161x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.13.0.md)
- [📈time plot](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.076x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-base.md)
- [📈time plot](bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1%2B-bedaea0-vs-base.svg)

