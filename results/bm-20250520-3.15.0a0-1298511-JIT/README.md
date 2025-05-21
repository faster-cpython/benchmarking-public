# Results

- fork: python/1298511b41ec0f9be925
- version: 3.15.0a0
- config: JIT
- commit hash: [1298511](https://github.com/python/cpython/commit/1298511)
- commit date: 2025-05-20T18:32:41-07:00
- commit merge base: [d327159eb4dd286973d10af93999de90a860880a](https://github.com/python/cpython/commit/d327159eb4dd286973d10af93999de90a860880a)
- ref: 1298511b41ec0f9be925

## linux x86_64 (azure)

- [pystats raw](bm-20250520-azure-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-pystats.json)
- [pystats table](bm-20250520-azure-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15165801319)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511.json)

### vs. 3.10.4

- Geometric mean: 1.311x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.10.4.md)
- [📈time plot](bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.083x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.12.0.md)
- [📈time plot](bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x slower (HPT: reliability of 96.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.13.0.md)
- [📈time plot](bm-20250520-linux-x86_64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15166592358)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511.json)

### vs. 3.10.4

- Geometric mean: 1.275x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.10.4.md)
- [📈time plot](bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x faster (HPT: reliability of 99.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.12.0.md)
- [📈time plot](bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.13.0.md)
- [📈time plot](bm-20250520-darwin-arm64-python-1298511b41ec0f9be925-3.15.0a0-1298511-vs-3.13.0.svg)

