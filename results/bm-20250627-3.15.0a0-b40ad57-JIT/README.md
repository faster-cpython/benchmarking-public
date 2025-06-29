# Results

- fork: brandtbucher/jit_nops
- version: 3.15.0a0
- config: JIT
- commit hash: [b40ad57](https://github.com/brandtbucher/cpython/commit/b40ad57)
- commit date: 2025-06-27T19:48:47-07:00
- commit merge base: [c419af9e277bea7dd78f4defefc752fe93b0b8ec](https://github.com/python/cpython/commit/c419af9e277bea7dd78f4defefc752fe93b0b8ec)
- ref: jit_nops

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15939681240)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57.json)

### vs. 3.10.4

- Geometric mean: 1.477x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-3.10.4.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.136x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-3.12.0.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-3.13.0.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-base-mem.svg)
- [📄table](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-base.md)
- [📈time plot](bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57-vs-base.svg)

