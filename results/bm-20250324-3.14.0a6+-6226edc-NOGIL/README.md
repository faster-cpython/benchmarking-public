# Results

- fork: python/6226edc48baa888b413f
- version: 3.14.0a6+
- config: NOGIL
- commit hash: [6226edc](https://github.com/python/cpython/commit/6226edc)
- commit date: 2025-03-24T14:04:45+00:00
- commit merge base: [78f1bac7f23b6d5a612ce569f35f3e0f3b36c9ab](https://github.com/python/cpython/commit/78f1bac7f23b6d5a612ce569f35f3e0f3b36c9ab)
- ref: 6226edc48baa888b413f

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14038046396)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6%2B-6226edc.json)

### vs. 3.10.4

- Geometric mean: 1.203x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6%2B-6226edc-vs-3.10.4.md)
- [📈time plot](bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6%2B-6226edc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x slower (HPT: reliability of 99.89%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6%2B-6226edc-vs-3.12.0.md)
- [📈time plot](bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6%2B-6226edc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x slower (HPT: reliability of 99.69%, 1.01x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6%2B-6226edc-vs-3.13.0.md)
- [📈time plot](bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6%2B-6226edc-vs-3.13.0.svg)

