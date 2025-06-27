# Results

- fork: python/8fdbbf8b18f1405abe67
- version: 3.15.0a0
- config: JIT
- commit hash: [8fdbbf8](https://github.com/python/cpython/commit/8fdbbf8)
- commit date: 2025-06-07T14:08:44-07:00
- commit merge base: [ac9c3431cc5916a795c42b3e2b965233ceffe6f0](https://github.com/python/cpython/commit/ac9c3431cc5916a795c42b3e2b965233ceffe6f0)
- ref: 8fdbbf8b18f1405abe67

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927032174)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json)

### vs. 3.10.4

- Geometric mean: 1.318x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.md)
- [📈time plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 98.06%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.md)
- [📈time plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 96.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.md)
- [📈time plot](bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927032174)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json)

### vs. 3.10.4

- Geometric mean: 1.459x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.122x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 99.15%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 69.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base-mem.svg)
- [📄table](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.md)
- [📈time plot](bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927032174)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json)

### vs. 3.10.4

- Geometric mean: 1.300x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.md)
- [📈time plot](bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.md)
- [📈time plot](bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.076x faster (HPT: reliability of 63.23%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.md)
- [📈time plot](bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8-vs-3.13.0.svg)

