# Results

- fork: brandtbucher/call_self_or_null
- version: 3.14.0a7+
- config: 
- commit hash: [1196dc5](https://github.com/brandtbucher/cpython/commit/1196dc5)
- commit date: 2025-04-16T10:40:29-07:00
- commit merge base: [62ff86fa55c903a8362a64ecc363d8443aff2d07](https://github.com/python/cpython/commit/62ff86fa55c903a8362a64ecc363d8443aff2d07)
- ref: call_self_or_null

## linux x86_64 (azure)

- [pystats raw](bm-20250416-azure-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-pystats.json)
- [pystats table](bm-20250416-azure-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-pystats.md)

### vs. base

- [pystats diff](bm-20250416-azure-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14499026326)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5.json)

### vs. 3.10.4

- Geometric mean: 1.452x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-3.10.4.md)
- [📈time plot](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.120x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-3.12.0.md)
- [📈time plot](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-3.13.0.md)
- [📈time plot](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 84.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-base-mem.svg)
- [📄table](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-base.md)
- [📈time plot](bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7%2B-1196dc5-vs-base.svg)

