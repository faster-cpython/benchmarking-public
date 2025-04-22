# Results

- fork: python/09b624b80f54e1f97812
- version: 3.14.0a7+
- config: JIT
- commit hash: [09b624b](https://github.com/python/cpython/commit/09b624b)
- commit date: 2025-04-21T15:59:03+01:00
- commit merge base: [70b322d3138311df53bc9fc57f174c8e9bdc2ab5](https://github.com/python/cpython/commit/70b322d3138311df53bc9fc57f174c8e9bdc2ab5)
- ref: 09b624b80f54e1f97812

## linux x86_64 (azure)

- [pystats raw](bm-20250421-azure-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-pystats.json)
- [pystats table](bm-20250421-azure-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14584839856)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b.json)

### vs. 3.10.4

- Geometric mean: 1.462x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-vs-3.10.4.md)
- [📈time plot](bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.127x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-vs-3.12.0.md)
- [📈time plot](bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-vs-3.13.0.md)
- [📈time plot](bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7%2B-09b624b-vs-3.13.0.svg)

