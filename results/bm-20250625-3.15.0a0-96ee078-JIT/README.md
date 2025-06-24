# Results

- fork: Fidget-Spinner/decref_for_nbody
- version: 3.15.0a0
- config: JIT
- commit hash: [96ee078](https://github.com/Fidget%2dSpinner/cpython/commit/96ee078)
- commit date: 2025-06-25T02:52:49+08:00
- commit merge base: [bda121862e7d7f4684d9f0281f7d1f408c0c740c](https://github.com/python/cpython/commit/bda121862e7d7f4684d9f0281f7d1f408c0c740c)
- ref: decref_for_nbody

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15860173623)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078.json)

### vs. 3.10.4

- Geometric mean: 1.471x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-3.10.4.md)
- [📈time plot](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.132x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-3.12.0.md)
- [📈time plot](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-3.13.0.md)
- [📈time plot](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 67.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-base-mem.svg)
- [📄table](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-base.md)
- [📈time plot](bm-20250625-linux-x86_64-Fidget%252dSpinner-decref_for_nbody-3.15.0a0-96ee078-vs-base.svg)

