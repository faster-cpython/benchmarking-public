# Results

- fork: python/98fa4a49fecbac3c990a
- version: 3.14.0a5+
- config: JIT
- commit hash: [98fa4a4](https://github.com/python/cpython/commit/98fa4a4)
- commit date: 2025-03-09T16:09:23-04:00
- commit merge base: [475f933ed8b1c9546f1b5497a2241140c7065b5f](https://github.com/python/cpython/commit/475f933ed8b1c9546f1b5497a2241140c7065b5f)
- ref: 98fa4a49fecbac3c990a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13771117967)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4.json)

### vs. 3.10.4

- Geometric mean: 1.309x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.10.4.md)
- [📈time plot](bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.45%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.12.0.md)
- [📈time plot](bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.13.0.md)
- [📈time plot](bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13771111380)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4.json)

### vs. 3.10.4

- Geometric mean: 1.379x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.10.4.md)
- [📈time plot](bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.12.0.md)
- [📈time plot](bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.13.0.md)
- [📈time plot](bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5%2B-98fa4a4-vs-3.13.0.svg)

