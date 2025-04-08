# Results

- fork: python/3b3720f1a26ab3437754
- version: 3.14.0a6+
- config: 
- commit hash: [3b3720f](https://github.com/python/cpython/commit/3b3720f)
- commit date: 2025-04-01T09:58:47+02:00
- commit merge base: [23a658b9af410b72beeb28ba4ace2d83896c5631](https://github.com/python/cpython/commit/23a658b9af410b72beeb28ba4ace2d83896c5631)
- ref: 3b3720f1a26ab3437754

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14340873020)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6%2B-3b3720f.json)

### vs. 3.10.4

- Geometric mean: 1.461x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6%2B-3b3720f-vs-3.10.4.md)
- [📈time plot](bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6%2B-3b3720f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.127x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6%2B-3b3720f-vs-3.12.0.md)
- [📈time plot](bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6%2B-3b3720f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6%2B-3b3720f-vs-3.13.0.md)
- [📈time plot](bm-20250401-linux-x86_64-python-3b3720f1a26ab3437754-3.14.0a6%2B-3b3720f-vs-3.13.0.svg)

