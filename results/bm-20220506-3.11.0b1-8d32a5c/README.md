# Results

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- version: 3.11.0b1
- commit hash: [8d32a5c](https://github.com/python/cpython/commit/8d32a5c)
- commit date: 2022-05-06T23:56:26+01:00
- ref: main
- commit date: 2022-05-06T22:56:26+00:00

## darwin arm64

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: coverage
- [table](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.md)
- [plot](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower
- missing benchmarks: coverage
- [table](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.md)
- [plot](bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c-vs-3.11.0.png)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-91-generic-x86_64-with-glibc2.31
- [raw results](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.10.4.md)
- [plot](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.11.0.md)
- [plot](bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c-vs-3.11.0.png)

