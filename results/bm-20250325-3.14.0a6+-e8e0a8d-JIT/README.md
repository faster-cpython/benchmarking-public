# Results

- fork: Fidget-Spinner/method_jit_2_5
- version: 3.14.0a6+
- config: JIT
- commit hash: [e8e0a8d](https://github.com/Fidget%2dSpinner/cpython/commit/e8e0a8d)
- commit date: 2025-03-25T21:56:51+08:00
- commit merge base: [ef06508f8ef1d2943b2fb1e310ab115b65e489a8](https://github.com/python/cpython/commit/ef06508f8ef1d2943b2fb1e310ab115b65e489a8)
- ref: method_jit_2_5

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14061983921)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d.json)

### vs. 3.10.4

- Geometric mean: 1.409x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, docutils, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-3.10.4.md)
- [📈time plot](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-3.12.0.md)
- [📈time plot](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 91.35%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, docutils, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-3.13.0.md)
- [📈time plot](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.022x slower (HPT: reliability of 99.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-base-mem.svg)
- [📄table](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-base.md)
- [📈time plot](bm-20250325-linux-x86_64-Fidget%252dSpinner-method_jit_2_5-3.14.0a6%2B-e8e0a8d-vs-base.svg)

