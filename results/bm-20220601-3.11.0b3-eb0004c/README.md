# Results

- fork: python
- ref: eb0004c27163ec089201
- version: 3.11.0b3
- commit hash: [eb0004c](https://github.com/python/cpython/commit/eb0004c)
- commit date: 2022-06-01T14:07:53+01:00
- ref: main
- commit date: 2022-06-01T13:07:53+00:00

## darwin arm64

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: coverage
- [table](bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c-vs-3.10.4.md)
- [plot](bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower
- missing benchmarks: coverage
- [table](bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c-vs-3.11.0.md)
- [plot](bm-20220601-darwin-arm64-python-eb0004c27163ec089201-3.11.0b3-eb0004c-vs-3.11.0.png)

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-91-generic-x86_64-with-glibc2.31
- [raw results](bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c-vs-3.10.4.md)
- [plot](bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c-vs-3.11.0.md)
- [plot](bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c-vs-3.11.0.png)

