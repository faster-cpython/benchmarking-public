# Results

- fork: iritkatriel/subscr_stats
- version: 3.14.0a6+
- config: 
- commit hash: [ebd800a](https://github.com/iritkatriel/cpython/commit/ebd800a)
- commit date: 2025-04-03T11:29:11+01:00
- commit merge base: [0cd4befb02df07c0b320cd6246227c13e57b2efb](https://github.com/python/cpython/commit/0cd4befb02df07c0b320cd6246227c13e57b2efb)
- ref: subscr_stats

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14241062283)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a.json)

### vs. 3.10.4

- Geometric mean: 1.454x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-3.10.4.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-3.12.0.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-3.13.0.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 83.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-base-mem.svg)
- [📄table](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-base.md)
- [📈time plot](bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6%2B-ebd800a-vs-base.svg)

