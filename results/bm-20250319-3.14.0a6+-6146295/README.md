# Results

- fork: python/6146295a5b8e9286ccb8
- version: 3.14.0a6+
- config: 
- commit hash: [6146295](https://github.com/python/cpython/commit/6146295)
- commit date: 2025-03-19T13:05:09-04:00
- commit merge base: [4b540313238de9d53bd9d9866eb481e954ad508f](https://github.com/python/cpython/commit/4b540313238de9d53bd9d9866eb481e954ad508f)
- ref: 6146295a5b8e9286ccb8

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13978995572)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295.json)

### vs. 3.10.4

- Geometric mean: 1.438x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.10.4.md)
- [📈time plot](bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.12.0.md)
- [📈time plot](bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.13.0.md)
- [📈time plot](bm-20250319-linux-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13971574699)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.10.4.md)
- [📈time plot](bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 73.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.12.0.md)
- [📈time plot](bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.13.0.md)
- [📈time plot](bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6%2B-6146295-vs-3.13.0.svg)

