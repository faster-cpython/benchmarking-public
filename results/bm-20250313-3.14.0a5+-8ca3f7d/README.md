# Results

- fork: faster-cpython/single_point_of_allo
- version: 3.14.0a5+
- config: 
- commit hash: [8ca3f7d](https://github.com/faster%2dcpython/cpython/commit/8ca3f7d)
- commit date: 2025-03-13T11:12:02+00:00
- commit merge base: [155c44b9015089eacc6e2ace449391c12bfb8b8d](https://github.com/python/cpython/commit/155c44b9015089eacc6e2ace449391c12bfb8b8d)
- ref: single_point_of_allo

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13833257599)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250313-pythonperf2-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-8ca3f7d.json)

### vs. 3.10.4

- Geometric mean: 1.250x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250313-pythonperf2-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-8ca3f7d-vs-3.10.4.md)
- [📈time plot](bm-20250313-pythonperf2-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-8ca3f7d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x slower (HPT: reliability of 99.49%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250313-pythonperf2-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-8ca3f7d-vs-3.12.0.md)
- [📈time plot](bm-20250313-pythonperf2-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-8ca3f7d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x slower (HPT: reliability of 97.45%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250313-pythonperf2-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-8ca3f7d-vs-3.13.0.md)
- [📈time plot](bm-20250313-pythonperf2-x86_64-faster%252dcpython-single_point_of_allo-3.14.0a5%2B-8ca3f7d-vs-3.13.0.svg)

