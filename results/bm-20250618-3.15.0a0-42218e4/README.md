# Results

- fork: mdboom/faster_pprint2
- version: 3.15.0a0
- config: 
- commit hash: [42218e4](https://github.com/mdboom/cpython/commit/42218e4)
- commit date: 2025-06-18T09:16:20-04:00
- commit merge base: [fba5dded6df3c2b1943557afef89a5cb418f65a2](https://github.com/python/cpython/commit/fba5dded6df3c2b1943557afef89a5cb418f65a2)
- ref: faster_pprint2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15733947517)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-3.10.4.md)
- [📈time plot](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-3.12.0.md)
- [📈time plot](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-3.13.0.md)
- [📈time plot](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-base-mem.svg)
- [📄table](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-base.md)
- [📈time plot](bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4-vs-base.svg)

