# Results

- fork: Fidget-Spinner/method_jit_bench
- version: 3.14.0a5+
- config: JIT
- commit hash: [2b1c0da](https://github.com/Fidget%2dSpinner/cpython/commit/2b1c0da)
- commit date: 2025-03-14T21:58:03+08:00
- commit merge base: [e0bc9d2a0c448cf46df233f8d84344c1f55a190f](https://github.com/python/cpython/commit/e0bc9d2a0c448cf46df233f8d84344c1f55a190f)
- ref: method_jit_bench

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13864750757)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da.json)

### vs. 3.10.4

- Geometric mean: 1.292x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-3.10.4.md)
- [📈time plot](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.453x slower (HPT: reliability of 100.00%, 1.78x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-3.12.0.md)
- [📈time plot](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.487x slower (HPT: reliability of 100.00%, 1.92x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: 2to3, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-3.13.0.md)
- [📈time plot](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.512x slower (HPT: reliability of 100.00%, 1.99x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 2to3
- [🧠memory plot](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-base-mem.svg)
- [📄table](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-base.md)
- [📈time plot](bm-20250314-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a5%2B-2b1c0da-vs-base.svg)

