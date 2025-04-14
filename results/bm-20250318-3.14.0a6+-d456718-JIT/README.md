# Results

- fork: Fidget-Spinner/method_jit_bench
- version: 3.14.0a6+
- config: JIT
- commit hash: [d456718](https://github.com/Fidget%2dSpinner/cpython/commit/d456718)
- commit date: 2025-03-18T00:37:21+08:00
- commit merge base: [b2ed7a6d6aae9860110f6ec495dc88dde670cfe4](https://github.com/python/cpython/commit/b2ed7a6d6aae9860110f6ec495dc88dde670cfe4)
- ref: method_jit_bench

## linux x86_64 (azure)

- [pystats raw](bm-20250318-azure-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-pystats.json)
- [pystats table](bm-20250318-azure-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13905200561)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718.json)

### vs. 3.10.4

- Geometric mean: 1.430x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-3.10.4.md)
- [📈time plot](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-3.12.0.md)
- [📈time plot](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 96.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: 2to3, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-3.13.0.md)
- [📈time plot](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x slower (HPT: reliability of 88.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 2to3
- [🧠memory plot](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-base-mem.svg)
- [📄table](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-base.md)
- [📈time plot](bm-20250318-linux-x86_64-Fidget%252dSpinner-method_jit_bench-3.14.0a6%2B-d456718-vs-base.svg)

