# Results

- fork: iritkatriel/subscr_stats
- version: 3.14.0a6+
- config: 
- commit hash: [1ae9389](https://github.com/iritkatriel/cpython/commit/1ae9389)
- commit date: 2025-04-03T20:29:38+01:00
- commit merge base: [0cd4befb02df07c0b320cd6246227c13e57b2efb](https://github.com/python/cpython/commit/0cd4befb02df07c0b320cd6246227c13e57b2efb)
- ref: subscr_stats

## linux x86_64 (azure)

- [pystats raw](bm-20250403-azure-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-pystats.json)
- [pystats table](bm-20250403-azure-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-pystats.md)

### vs. base

- [pystats diff](bm-20250403-azure-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14259155879)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-3.10.4.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-3.12.0.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-3.13.0.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 72.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-base-mem.svg)
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-base.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-1ae9389-vs-base.svg)

