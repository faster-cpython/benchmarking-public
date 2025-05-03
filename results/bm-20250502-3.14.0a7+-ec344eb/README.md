# Results

- fork: iritkatriel/array_subscr
- version: 3.14.0a7+
- config: 
- commit hash: [ec344eb](https://github.com/iritkatriel/cpython/commit/ec344eb)
- commit date: 2025-05-02T22:49:32+01:00
- commit merge base: [49ea8a0b2d5d65122e5e661be8a2ff9809c09cc0](https://github.com/python/cpython/commit/49ea8a0b2d5d65122e5e661be8a2ff9809c09cc0)
- ref: array_subscr

## linux x86_64 (azure)

- [pystats raw](bm-20250502-azure-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-pystats.json)
- [pystats table](bm-20250502-azure-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-pystats.md)

### vs. base

- [pystats diff](bm-20250502-azure-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14803946352)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-3.10.4.md)
- [📈time plot](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.117x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-3.12.0.md)
- [📈time plot](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, coverage, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-3.13.0.md)
- [📈time plot](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 89.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 coverage, sqlalchemy_declarative, sqlalchemy_imperative
- [🧠memory plot](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-base-mem.svg)
- [📄table](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-base.md)
- [📈time plot](bm-20250502-linux-x86_64-iritkatriel-array_subscr-3.14.0a7%2B-ec344eb-vs-base.svg)

