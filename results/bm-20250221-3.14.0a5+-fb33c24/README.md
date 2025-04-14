# Results

- fork: iritkatriel/stats
- version: 3.14.0a5+
- config: 
- commit hash: [fb33c24](https://github.com/iritkatriel/cpython/commit/fb33c24)
- commit date: 2025-02-21T15:53:01+00:00
- commit merge base: [5d66c55c8ad0a0aeff8d06021ddca1d02c5f4416](https://github.com/python/cpython/commit/5d66c55c8ad0a0aeff8d06021ddca1d02c5f4416)
- ref: stats

## linux x86_64 (azure)

- [pystats raw](bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-pystats.json)

### vs. base

- [pystats diff](bm-20250221-azure-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14215475552)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24.json)

### vs. 3.10.4

- Geometric mean: 1.439x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-3.10.4.md)
- [📈time plot](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-3.12.0.md)
- [📈time plot](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-3.13.0.md)
- [📈time plot](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-base-mem.svg)
- [📄table](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-base.md)
- [📈time plot](bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5%2B-fb33c24-vs-base.svg)

