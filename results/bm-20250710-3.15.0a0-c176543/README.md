# Results

- fork: python/c17654334946b232aa29
- version: 3.15.0a0
- config: 
- commit hash: [c176543](https://github.com/python/cpython/commit/c176543)
- commit date: 2025-07-10T11:57:29+03:00
- commit merge base: [b44316a0976fb3fcd50bae9d67b0810ee0252d93](https://github.com/python/cpython/commit/b44316a0976fb3fcd50bae9d67b0810ee0252d93)
- ref: c17654334946b232aa29

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16193666264)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.10.4.md)
- [📈time plot](bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.12.0.md)
- [📈time plot](bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.13.0.md)
- [📈time plot](bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16196041824)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543.json)

### vs. 3.10.4

- Geometric mean: 1.252x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.10.4.md)
- [📈time plot](bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 94.84%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.12.0.md)
- [📈time plot](bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x slower (HPT: reliability of 61.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.13.0.md)
- [📈time plot](bm-20250710-darwin-arm64-python-c17654334946b232aa29-3.15.0a0-c176543-vs-3.13.0.svg)

