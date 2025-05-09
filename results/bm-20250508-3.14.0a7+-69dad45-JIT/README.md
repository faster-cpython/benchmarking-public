# Results

- fork: Fidget-Spinner/outline
- version: 3.14.0a7+
- config: JIT
- commit hash: [69dad45](https://github.com/Fidget%2dSpinner/cpython/commit/69dad45)
- commit date: 2025-05-08T04:38:37+08:00
- commit merge base: [3dfed230928de0f649061782a36691066a0ef058](https://github.com/python/cpython/commit/3dfed230928de0f649061782a36691066a0ef058)
- ref: outline

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14919697048)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45.json)

### vs. 3.10.4

- Geometric mean: 1.418x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-3.10.4.md)
- [📈time plot](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-3.12.0.md)
- [📈time plot](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x faster (HPT: reliability of 75.22%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-3.13.0.md)
- [📈time plot](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-base-mem.svg)
- [📄table](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-base.md)
- [📈time plot](bm-20250508-linux-x86_64-Fidget%252dSpinner-outline-3.14.0a7%2B-69dad45-vs-base.svg)

