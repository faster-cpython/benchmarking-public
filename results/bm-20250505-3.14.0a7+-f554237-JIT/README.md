# Results

- fork: python/f554237b8ef6c60df651
- version: 3.14.0a7+
- config: JIT
- commit hash: [f554237](https://github.com/python/cpython/commit/f554237)
- commit date: 2025-05-05T13:44:50+01:00
- commit merge base: [8d5f3cd2ce6b6af26d3882b8a21afba0a3f4c22f](https://github.com/python/cpython/commit/8d5f3cd2ce6b6af26d3882b8a21afba0a3f4c22f)
- ref: f554237b8ef6c60df651

## linux x86_64 (azure)

- [pystats raw](bm-20250505-azure-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-pystats.json)
- [pystats table](bm-20250505-azure-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14852529273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-vs-3.10.4.md)
- [📈time plot](bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-vs-3.12.0.md)
- [📈time plot](bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.58%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-vs-3.13.0.md)
- [📈time plot](bm-20250505-linux-x86_64-python-f554237b8ef6c60df651-3.14.0a7%2B-f554237-vs-3.13.0.svg)

