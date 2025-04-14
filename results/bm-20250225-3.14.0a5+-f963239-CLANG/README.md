# Results

- fork: python/f963239ff1f986742d4c
- version: 3.14.0a5+
- config: CLANG
- commit hash: [f963239](https://github.com/python/cpython/commit/f963239)
- commit date: 2025-02-25T12:03:28-05:00
- commit merge base: [c5f925c8c948736bd64652918b4e0186b91abbb5](https://github.com/python/cpython/commit/c5f925c8c948736bd64652918b4e0186b91abbb5)
- ref: f963239ff1f986742d4c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13903722591)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5%2B-f963239.json)

### vs. 3.10.4

- Geometric mean: 1.489x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5%2B-f963239-vs-3.10.4.md)
- [📈time plot](bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5%2B-f963239-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.149x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5%2B-f963239-vs-3.12.0.md)
- [📈time plot](bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5%2B-f963239-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5%2B-f963239-vs-3.13.0.md)
- [📈time plot](bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5%2B-f963239-vs-3.13.0.svg)

