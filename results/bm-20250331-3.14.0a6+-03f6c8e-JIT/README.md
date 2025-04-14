# Results

- fork: python/03f6c8e239723637811f
- version: 3.14.0a6+
- config: JIT
- commit hash: [03f6c8e](https://github.com/python/cpython/commit/03f6c8e)
- commit date: 2025-03-31T18:29:12+00:00
- commit merge base: [0cd4befb02df07c0b320cd6246227c13e57b2efb](https://github.com/python/cpython/commit/0cd4befb02df07c0b320cd6246227c13e57b2efb)
- ref: 03f6c8e239723637811f

## linux x86_64 (azure)

- [pystats raw](bm-20250331-azure-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-pystats.json)
- [pystats table](bm-20250331-azure-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-pystats.md)

### vs. base

- [pystats diff](bm-20250331-azure-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14178800386)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e.json)

### vs. 3.10.4

- Geometric mean: 1.469x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-3.10.4.md)
- [📈time plot](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-3.12.0.md)
- [📈time plot](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-3.13.0.md)
- [📈time plot](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.87%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-base-mem.svg)
- [📄table](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-base.md)
- [📈time plot](bm-20250331-linux-x86_64-python-03f6c8e239723637811f-3.14.0a6%2B-03f6c8e-vs-base.svg)

