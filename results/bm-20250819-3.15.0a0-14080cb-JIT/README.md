# Results

- fork: faster-cpython/jit_trampoline
- version: 3.15.0a0
- config: JIT
- commit hash: [14080cb](https://github.com/faster%2dcpython/cpython/commit/14080cb)
- commit date: 2025-08-19T16:09:23+01:00
- commit merge base: [719e5c3f7111bcda5eee72fe648786c427c4d4c2](https://github.com/python/cpython/commit/719e5c3f7111bcda5eee72fe648786c427c4d4c2)
- ref: jit_trampoline

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17075861575)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.10.4.md)
- [📈time plot](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.12.0.md)
- [📈time plot](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.13.0.md)
- [📈time plot](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-base-mem.svg)
- [📄table](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-base.md)
- [📈time plot](bm-20250819-pythonperf2-x86_64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17075844720)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.10.4.md)
- [📈time plot](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.128x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.12.0.md)
- [📈time plot](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.082x faster (HPT: reliability of 89.29%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.13.0.md)
- [📈time plot](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 68.04%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-base.md)
- [📈time plot](bm-20250819-pythonperf1-amd64-faster%252dcpython-jit_trampoline-3.15.0a0-14080cb-vs-base.svg)

