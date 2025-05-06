# Results

- fork: python/b1aa515bd6b645202eda
- version: 3.14.0a7+
- config: JIT
- commit hash: [b1aa515](https://github.com/python/cpython/commit/b1aa515)
- commit date: 2025-05-05T15:25:22-07:00
- commit merge base: [f9b22bb79d8a233380bc5eb3820bf846404a7258](https://github.com/python/cpython/commit/f9b22bb79d8a233380bc5eb3820bf846404a7258)
- ref: b1aa515bd6b645202eda

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14852534960)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7%2B-b1aa515.json)

### vs. 3.10.4

- Geometric mean: 1.462x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7%2B-b1aa515-vs-3.10.4.md)
- [📈time plot](bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7%2B-b1aa515-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7%2B-b1aa515-vs-3.12.0.md)
- [📈time plot](bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7%2B-b1aa515-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x faster (HPT: reliability of 98.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, coverage, djangocms, gevent_hub, gunicorn, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7%2B-b1aa515-vs-3.13.0.md)
- [📈time plot](bm-20250505-linux-x86_64-python-b1aa515bd6b645202eda-3.14.0a7%2B-b1aa515-vs-3.13.0.svg)

