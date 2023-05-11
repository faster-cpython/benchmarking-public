# Results

- fork: python
- version: 3.11.0b1
- commit hash: [8d32a5c](https://github.com/python/cpython/commit/8d32a5c)
- commit date: 2022-05-06T23:56:26+01:00
- commit date: 2022-05-06T22:56:26+00:00
- ref: 8d32a5c8c4e9c90b0a21, main

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-91-generic-x86_64-with-glibc2.31
- [raw results](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols
- [table](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.10.4.md)
- [plot](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols
- [table](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.11.0.md)
- [plot](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513535796)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c.json)

### vs. 3.10.4

- 1.23x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.md)
- [plot](bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.md)
- [plot](bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4483411100)
- cpu model: missing
- platform: Windows-10-10.0.22000-SP0
- [raw results](bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c.json)

### vs. 3.10.4

- 1.09x faster \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.md)
- [plot](bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: asyncio_tcp_ssl, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.md)
- [plot](bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494503699)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c.json)

### vs. 3.10.4

- 1.19x faster \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.md)
- [plot](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower \*
- missing benchmarks: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.md)
- [plot](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.png)

