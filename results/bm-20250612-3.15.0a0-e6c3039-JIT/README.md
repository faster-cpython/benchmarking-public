# Results

- fork: python/e6c3039cb39e68ae9af9
- version: 3.15.0a0
- config: JIT
- commit hash: [e6c3039](https://github.com/python/cpython/commit/e6c3039)
- commit date: 2025-06-12T16:41:05+05:30
- commit merge base: [d4471297586335d8c24db8b2c030d32c94570344](https://github.com/python/cpython/commit/d4471297586335d8c24db8b2c030d32c94570344)
- ref: e6c3039cb39e68ae9af9

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15633690478)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039.json)

### vs. 3.10.4

- Geometric mean: 1.326x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039-vs-3.10.4.md)
- [📈time plot](bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039-vs-3.12.0.md)
- [📈time plot](bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 97.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039-vs-3.13.0.md)
- [📈time plot](bm-20250612-linux-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039-vs-3.13.0.svg)

