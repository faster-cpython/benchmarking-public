# Results

- fork: iritkatriel/dicts
- version: 3.14.0a6+
- config: 
- commit hash: [bf2d1dd](https://github.com/iritkatriel/cpython/commit/bf2d1dd)
- commit date: 2025-04-10T19:21:36+01:00
- commit merge base: [f0dcb29d3affbbe1ec25b922235f0556bd695067](https://github.com/python/cpython/commit/f0dcb29d3affbbe1ec25b922235f0556bd695067)
- ref: dicts

## linux x86_64 (azure)

- [pystats raw](bm-20250410-azure-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-pystats.json)
- [pystats table](bm-20250410-azure-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-pystats.md)

### vs. base

- [pystats diff](bm-20250410-azure-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14388783585)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd.json)

### vs. 3.10.4

- Geometric mean: 1.479x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-3.10.4.md)
- [📈time plot](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.141x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-3.12.0.md)
- [📈time plot](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.068x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-3.13.0.md)
- [📈time plot](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-base-mem.svg)
- [📄table](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-base.md)
- [📈time plot](bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6%2B-bf2d1dd-vs-base.svg)

