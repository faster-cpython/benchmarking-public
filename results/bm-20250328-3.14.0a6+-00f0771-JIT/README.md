# Results

- fork: python/00f0771e4dbd8c8b66b3
- version: 3.14.0a6+
- config: JIT
- commit hash: [00f0771](https://github.com/python/cpython/commit/00f0771)
- commit date: 2025-03-28T14:59:03-04:00
- commit merge base: [d260631be063d97f1a6d1c8f9fa2ce9b0e4f8a58](https://github.com/python/cpython/commit/d260631be063d97f1a6d1c8f9fa2ce9b0e4f8a58)
- ref: 00f0771e4dbd8c8b66b3

## linux x86_64 (azure)

- [pystats raw](bm-20250328-azure-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-pystats.json)
- [pystats table](bm-20250328-azure-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-pystats.md)

### vs. base

- [pystats diff](bm-20250328-azure-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14162637777)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771.json)

### vs. 3.10.4

- Geometric mean: 1.467x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-3.10.4.md)
- [📈time plot](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-3.12.0.md)
- [📈time plot](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-3.13.0.md)
- [📈time plot](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 78.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-base-mem.svg)
- [📄table](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-base.md)
- [📈time plot](bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6%2B-00f0771-vs-base.svg)

