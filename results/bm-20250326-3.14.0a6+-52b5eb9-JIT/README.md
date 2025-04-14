# Results

- fork: python/52b5eb95b770fa00ebbd
- version: 3.14.0a6+
- config: JIT
- commit hash: [52b5eb9](https://github.com/python/cpython/commit/52b5eb9)
- commit date: 2025-03-26T22:49:28+02:00
- commit merge base: [4b3d5b604210f68005ef64d5346ca169385f5acf](https://github.com/python/cpython/commit/4b3d5b604210f68005ef64d5346ca169385f5acf)
- ref: 52b5eb95b770fa00ebbd

## linux x86_64 (azure)

- [pystats raw](bm-20250326-azure-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-pystats.json)
- [pystats table](bm-20250326-azure-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-pystats.md)

### vs. base

- [pystats diff](bm-20250326-azure-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14115511011)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9.json)

### vs. 3.10.4

- Geometric mean: 1.323x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-vs-3.10.4.md)
- [📈time plot](bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 95.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-vs-3.12.0.md)
- [📈time plot](bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-vs-3.13.0.md)
- [📈time plot](bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6%2B-52b5eb9-vs-3.13.0.svg)

