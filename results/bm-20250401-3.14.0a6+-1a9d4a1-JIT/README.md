# Results

- fork: python/1a9d4a1fb3d4beda7c7e
- version: 3.14.0a6+
- config: JIT
- commit hash: [1a9d4a1](https://github.com/python/cpython/commit/1a9d4a1)
- commit date: 2025-04-01T15:10:15-07:00
- commit merge base: [cd69d55f64087f74da816eaf20c34ddeabfdb2bb](https://github.com/python/cpython/commit/cd69d55f64087f74da816eaf20c34ddeabfdb2bb)
- ref: 1a9d4a1fb3d4beda7c7e

## linux x86_64 (azure)

- [pystats raw](bm-20250401-azure-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-pystats.json)
- [pystats table](bm-20250401-azure-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-pystats.md)

### vs. base

- [pystats diff](bm-20250401-azure-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14209259473)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1.json)

### vs. 3.10.4

- Geometric mean: 1.470x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-3.10.4.md)
- [📈time plot](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-3.12.0.md)
- [📈time plot](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-3.13.0.md)
- [📈time plot](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-base-mem.svg)
- [📄table](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-base.md)
- [📈time plot](bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6%2B-1a9d4a1-vs-base.svg)

