# Results

- fork: faster-cpython/tier_2_tos_caching
- version: 3.15.0a0
- config: JIT
- commit hash: [efe4628](https://github.com/faster%2dcpython/cpython/commit/efe4628)
- commit date: 2025-08-22T08:34:25+01:00
- commit merge base: [a8d9d947843200a09c154f3bc55f4e87e35edab3](https://github.com/python/cpython/commit/a8d9d947843200a09c154f3bc55f4e87e35edab3)
- ref: tier_2_tos_caching

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17150117325)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250822-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250822-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.10.4.md)
- [📈time plot](bm-20250822-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250822-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.12.0.md)
- [📈time plot](bm-20250822-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 99.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250822-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.13.0.md)
- [📈time plot](bm-20250822-arminc-aarch64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17150140176)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250822-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json)

### vs. 3.10.4

- Geometric mean: 1.344x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250822-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.10.4.md)
- [📈time plot](bm-20250822-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250822-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.12.0.md)
- [📈time plot](bm-20250822-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250822-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.13.0.md)
- [📈time plot](bm-20250822-pythonperf2-x86_64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17150126139)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json)

### vs. 3.10.4

- Geometric mean: 1.324x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.10.4.md)
- [📈time plot](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.131x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.12.0.md)
- [📈time plot](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.085x faster (HPT: reliability of 86.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.13.0.md)
- [📈time plot](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 pycparser
- [📄table](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-base.md)
- [📈time plot](bm-20250822-pythonperf1-amd64-faster%252dcpython-tier_2_tos_caching-3.15.0a0-efe4628-vs-base.svg)

