# Results

- fork: iritkatriel/stats
- version: 3.14.0a6+
- config: 
- commit hash: [4300c89](https://github.com/iritkatriel/cpython/commit/4300c89)
- commit date: 2025-04-06T23:23:53+01:00
- commit merge base: [7bb1e1a23634bae81bf76fdb34e9f9f7e59b3793](https://github.com/python/cpython/commit/7bb1e1a23634bae81bf76fdb34e9f9f7e59b3793)
- ref: stats

## linux x86_64 (azure)

- [pystats raw](bm-20250406-azure-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-pystats.json)
- [pystats table](bm-20250406-azure-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-pystats.md)

### vs. base

- [pystats diff](bm-20250406-azure-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14297206278)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89.json)

### vs. 3.10.4

- Geometric mean: 1.466x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-3.10.4.md)
- [📈time plot](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-3.12.0.md)
- [📈time plot](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-3.13.0.md)
- [📈time plot](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-base-mem.svg)
- [📄table](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-base.md)
- [📈time plot](bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6%2B-4300c89-vs-base.svg)

