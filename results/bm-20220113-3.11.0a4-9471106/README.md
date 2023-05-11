# Results

- fork: python
- version: 3.11.0a4
- commit hash: [9471106](https://github.com/python/cpython/commit/9471106)
- commit date: 2022-01-13T19:38:15+00:00
- ref: 9471106fd5b47418ffd2, main

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-91-generic-x86_64-with-glibc2.31
- [raw results](bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106.json)

### vs. 3.10.4

- 1.24x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols
- [table](bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106-vs-3.10.4.md)
- [plot](bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x slower \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols
- [table](bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106-vs-3.11.0.md)
- [plot](bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513535430)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20220113-pythonperf2-x86_64-python-9471106fd5b47418ffd2-3.11.0a4-9471106.json)

### vs. 3.10.4

- 1.15x faster \*
- missing benchmarks: asyncio_tcp_ssl, mypy2, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220113-pythonperf2-x86_64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.10.4.md)
- [plot](bm-20220113-pythonperf2-x86_64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.10.4.png)

### vs. 3.11.0

- 1.06x slower \*
- missing benchmarks: asyncio_tcp_ssl, mypy2, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220113-pythonperf2-x86_64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.11.0.md)
- [plot](bm-20220113-pythonperf2-x86_64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494503317)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20220113-darwin-arm64-python-9471106fd5b47418ffd2-3.11.0a4-9471106.json)

### vs. 3.10.4

- 1.16x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220113-darwin-arm64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.10.4.md)
- [plot](bm-20220113-darwin-arm64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20220113-darwin-arm64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.11.0.md)
- [plot](bm-20220113-darwin-arm64-python-9471106fd5b47418ffd2-3.11.0a4-9471106-vs-3.11.0.png)

