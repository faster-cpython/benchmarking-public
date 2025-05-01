# Results

- fork: sergey-miryanov/gh_132042_optimize_c
- version: 3.14.0a7+
- config: 
- commit hash: [04539cc](https://github.com/sergey%2dmiryanov/cpython/commit/04539cc)
- commit date: 2025-05-01T00:30:44+05:00
- commit merge base: [94b4fcd806e7b692955173d309ea3b70a193ad96](https://github.com/python/cpython/commit/94b4fcd806e7b692955173d309ea3b70a193ad96)
- ref: gh_132042_optimize_c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14775917643)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc.json)

### vs. 3.10.4

- Geometric mean: 1.441x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-3.10.4.md)
- [📈time plot](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.112x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-3.12.0.md)
- [📈time plot](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-3.13.0.md)
- [📈time plot](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 96.30%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-base-mem.svg)
- [📄table](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-base.md)
- [📈time plot](bm-20250501-linux-x86_64-sergey%252dmiryanov-gh_132042_optimize_c-3.14.0a7%2B-04539cc-vs-base.svg)

