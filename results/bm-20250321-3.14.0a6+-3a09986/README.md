# Results

- fork: python/3a09986553dd7778cae4
- version: 3.14.0a6+
- config: 
- commit hash: [3a09986](https://github.com/python/cpython/commit/3a09986)
- commit date: 2025-03-21T16:24:15+01:00
- commit merge base: [4f325168048fda89cef8bd2de859f65ec91754a3](https://github.com/python/cpython/commit/4f325168048fda89cef8bd2de859f65ec91754a3)
- ref: 3a09986553dd7778cae4

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13999317284)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250321-pythonperf2-x86_64-python-3a09986553dd7778cae4-3.14.0a6%2B-3a09986.json)

### vs. 3.10.4

- Geometric mean: 1.324x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250321-pythonperf2-x86_64-python-3a09986553dd7778cae4-3.14.0a6%2B-3a09986-vs-3.10.4.md)
- [📈time plot](bm-20250321-pythonperf2-x86_64-python-3a09986553dd7778cae4-3.14.0a6%2B-3a09986-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 97.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250321-pythonperf2-x86_64-python-3a09986553dd7778cae4-3.14.0a6%2B-3a09986-vs-3.12.0.md)
- [📈time plot](bm-20250321-pythonperf2-x86_64-python-3a09986553dd7778cae4-3.14.0a6%2B-3a09986-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250321-pythonperf2-x86_64-python-3a09986553dd7778cae4-3.14.0a6%2B-3a09986-vs-3.13.0.md)
- [📈time plot](bm-20250321-pythonperf2-x86_64-python-3a09986553dd7778cae4-3.14.0a6%2B-3a09986-vs-3.13.0.svg)

