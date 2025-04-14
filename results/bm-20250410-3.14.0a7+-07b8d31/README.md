# Results

- fork: python/07b8d3117fdbc4e5be55
- version: 3.14.0a7+
- config: 
- commit hash: [07b8d31](https://github.com/python/cpython/commit/07b8d31)
- commit date: 2025-04-10T21:13:26-07:00
- commit merge base: [e5f68fd29b3bd867207f23608a8dbc5759a056ed](https://github.com/python/cpython/commit/e5f68fd29b3bd867207f23608a8dbc5759a056ed)
- ref: 07b8d3117fdbc4e5be55

## linux x86_64 (azure)

- [pystats raw](bm-20250410-azure-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-pystats.json)
- [pystats table](bm-20250410-azure-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14420505269)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31.json)

### vs. 3.10.4

- Geometric mean: 1.459x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.10.4.md)
- [📈time plot](bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.125x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.12.0.md)
- [📈time plot](bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.054x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.13.0.md)
- [📈time plot](bm-20250410-linux-x86_64-python-07b8d3117fdbc4e5be55-3.14.0a7%2B-07b8d31-vs-3.13.0.svg)

