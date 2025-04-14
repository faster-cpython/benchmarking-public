# Results

- fork: mdboom/set_lookkey
- version: 3.14.0a6+
- config: 
- commit hash: [fc62499](https://github.com/mdboom/cpython/commit/fc62499)
- commit date: 2025-03-25T12:10:36-04:00
- commit merge base: [7c3692fe275088e986f92cec34dcccb823b31fa2](https://github.com/python/cpython/commit/7c3692fe275088e986f92cec34dcccb823b31fa2)
- ref: set_lookkey

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14064613874)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499.json)

### vs. 3.10.4

- Geometric mean: 1.431x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-3.10.4.md)
- [📈time plot](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.105x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-3.12.0.md)
- [📈time plot](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.69%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-3.13.0.md)
- [📈time plot](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 86.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-base-mem.svg)
- [📄table](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-base.md)
- [📈time plot](bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6%2B-fc62499-vs-base.svg)

