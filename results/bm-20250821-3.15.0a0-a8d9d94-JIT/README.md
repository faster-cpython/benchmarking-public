# Results

- fork: python/a8d9d947843200a09c15
- version: 3.15.0a0
- config: JIT
- commit hash: [a8d9d94](https://github.com/python/cpython/commit/a8d9d94)
- commit date: 2025-08-21T10:40:53+01:00
- commit merge base: [c056a089d8573b03c62d52ee05f48bf6804da66b](https://github.com/python/cpython/commit/c056a089d8573b03c62d52ee05f48bf6804da66b)
- ref: a8d9d947843200a09c15

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17150117325)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94.json)

### vs. 3.10.4

- Geometric mean: 1.300x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.md)
- [📈time plot](bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 99.90%, 1.01x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.md)
- [📈time plot](bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 99.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.md)
- [📈time plot](bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17150140176)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94.json)

### vs. 3.10.4

- Geometric mean: 1.334x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.md)
- [📈time plot](bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.md)
- [📈time plot](bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.md)
- [📈time plot](bm-20250821-pythonperf2-x86_64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17150126139)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.md)
- [📈time plot](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.md)
- [📈time plot](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.089x faster (HPT: reliability of 95.77%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.md)
- [📈time plot](bm-20250821-pythonperf1-amd64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94-vs-3.13.0.svg)

