# Results

- fork: brandtbucher/setlist
- version: 3.14.0a7+
- config: 
- commit hash: [7b2de0a](https://github.com/brandtbucher/cpython/commit/7b2de0a)
- commit date: 2025-04-17T11:04:43-07:00
- commit merge base: [62ff86fa55c903a8362a64ecc363d8443aff2d07](https://github.com/python/cpython/commit/62ff86fa55c903a8362a64ecc363d8443aff2d07)
- ref: setlist

## linux x86_64 (azure)

- [pystats raw](bm-20250417-azure-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-pystats.json)
- [pystats table](bm-20250417-azure-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-pystats.md)

### vs. base

- [pystats diff](bm-20250417-azure-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14521953107)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a.json)

### vs. 3.10.4

- Geometric mean: 1.461x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-3.10.4.md)
- [📈time plot](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.126x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-3.12.0.md)
- [📈time plot](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-3.13.0.md)
- [📈time plot](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 96.35%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-base-mem.svg)
- [📄table](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-base.md)
- [📈time plot](bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7%2B-7b2de0a-vs-base.svg)

