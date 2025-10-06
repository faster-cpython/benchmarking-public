# Results

- fork: python/880c9526f91960b9cba5
- version: 3.15.0a0
- config: NOGIL
- commit hash: [880c952](https://github.com/python/cpython/commit/880c952)
- commit date: 2025-10-04T22:06:56+01:00
- commit merge base: [0b2168275e8ec491fe7ea6f8c662e804437dfdab](https://github.com/python/cpython/commit/0b2168275e8ec491fe7ea6f8c662e804437dfdab)
- ref: 880c9526f91960b9cba5

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18251183585)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json)

### vs. 3.10.4

- Geometric mean: 1.207x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.67x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.10.4.md)
- [📈time plot](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x slower (HPT: reliability of 84.34%, 1.00x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.12.0.md)
- [📈time plot](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x slower (HPT: reliability of 90.31%, 1.00x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.13.0.md)
- [📈time plot](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-base-mem.svg)
- [📄table](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-base.md)
- [📈time plot](bm-20251004-pythonperf2-x86_64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18251183585)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json)

### vs. 3.10.4

- Geometric mean: 1.201x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.10.4.md)
- [📈time plot](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 81.22%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.12.0.md)
- [📈time plot](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x slower (HPT: reliability of 99.87%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.13.0.md)
- [📈time plot](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.091x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-base.md)
- [📈time plot](bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/18251183585)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json)

### vs. 3.10.4

- Geometric mean: 1.331x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.10.4.md)
- [📈time plot](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.364x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.12.0.md)
- [📈time plot](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.152x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.13.0.md)
- [📈time plot](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-base.md)
- [📈time plot](bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952-vs-base.svg)

