# Results

- fork: python/ce79274e9f093bd06d22
- version: 3.14.0a6+
- config: 
- commit hash: [ce79274](https://github.com/python/cpython/commit/ce79274)
- commit date: 2025-03-20T17:06:21+00:00
- commit merge base: [f53e7de6a84a0f535efb75c3671283b801a1af0f](https://github.com/python/cpython/commit/f53e7de6a84a0f535efb75c3671283b801a1af0f)
- ref: ce79274e9f093bd06d22

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13992120783)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6%2B-ce79274.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6%2B-ce79274-vs-3.10.4.md)
- [📈time plot](bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6%2B-ce79274-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 74.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6%2B-ce79274-vs-3.12.0.md)
- [📈time plot](bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6%2B-ce79274-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6%2B-ce79274-vs-3.13.0.md)
- [📈time plot](bm-20250320-pythonperf2-x86_64-python-ce79274e9f093bd06d22-3.14.0a6%2B-ce79274-vs-3.13.0.svg)

