# Results

- fork: fluhus/amit
- version: 3.14.0a6+
- config: JIT
- commit hash: [138f037](https://github.com/fluhus/cpython/commit/138f037)
- commit date: 2025-03-29T08:43:01-07:00
- commit merge base: [8a00c9a4d2ce9d373b13f8f0a2265a65f4523293](https://github.com/python/cpython/commit/8a00c9a4d2ce9d373b13f8f0a2265a65f4523293)
- ref: amit

## linux x86_64 (azure)

- [pystats raw](bm-20250329-azure-x86_64-fluhus-amit-3.14.0a6%2B-138f037-pystats.json)
- [pystats table](bm-20250329-azure-x86_64-fluhus-amit-3.14.0a6%2B-138f037-pystats.md)

### vs. base

- [pystats diff](bm-20250329-azure-x86_64-fluhus-amit-3.14.0a6%2B-138f037-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14148500234)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037.json)

### vs. 3.10.4

- Geometric mean: 1.465x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-3.10.4.md)
- [📈time plot](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-3.12.0.md)
- [📈time plot](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x faster (HPT: reliability of 99.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-3.13.0.md)
- [📈time plot](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 97.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-base-mem.svg)
- [📄table](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-base.md)
- [📈time plot](bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6%2B-138f037-vs-base.svg)

