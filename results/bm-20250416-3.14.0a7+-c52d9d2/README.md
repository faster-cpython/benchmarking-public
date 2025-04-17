# Results

- fork: iritkatriel/list_subscr
- version: 3.14.0a7+
- config: 
- commit hash: [c52d9d2](https://github.com/iritkatriel/cpython/commit/c52d9d2)
- commit date: 2025-04-16T23:00:23+01:00
- commit merge base: [62ff86fa55c903a8362a64ecc363d8443aff2d07](https://github.com/python/cpython/commit/62ff86fa55c903a8362a64ecc363d8443aff2d07)
- ref: list_subscr

## linux x86_64 (azure)

- [pystats raw](bm-20250416-azure-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-pystats.json)
- [pystats table](bm-20250416-azure-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-pystats.md)

### vs. base

- [pystats diff](bm-20250416-azure-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14503477605)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2.json)

### vs. 3.10.4

- Geometric mean: 1.461x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-3.10.4.md)
- [📈time plot](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.126x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-3.12.0.md)
- [📈time plot](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-3.13.0.md)
- [📈time plot](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 78.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-base-mem.svg)
- [📄table](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-base.md)
- [📈time plot](bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7%2B-c52d9d2-vs-base.svg)

