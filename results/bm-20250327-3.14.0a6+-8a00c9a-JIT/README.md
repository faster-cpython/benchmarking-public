# Results

- fork: python/8a00c9a4d2ce9d373b13
- version: 3.14.0a6+
- config: JIT
- commit hash: [8a00c9a](https://github.com/python/cpython/commit/8a00c9a)
- commit date: 2025-03-27T21:06:52+02:00
- commit merge base: [972a295fe34280aa3d16c573d6200025a1ce4ff0](https://github.com/python/cpython/commit/972a295fe34280aa3d16c573d6200025a1ce4ff0)
- ref: 8a00c9a4d2ce9d373b13

## linux x86_64 (azure)

- [pystats raw](bm-20250327-azure-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-pystats.json)
- [pystats table](bm-20250327-azure-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14117422276)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a.json)

### vs. 3.10.4

- Geometric mean: 1.460x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-vs-3.10.4.md)
- [📈time plot](bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.127x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-vs-3.12.0.md)
- [📈time plot](bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 99.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-vs-3.13.0.md)
- [📈time plot](bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6%2B-8a00c9a-vs-3.13.0.svg)

