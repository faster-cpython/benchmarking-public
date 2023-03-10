# Results

- fork: python
- ref: main
- version: 3.11.0a6
- commit hash: [3ddfa55](https://github.com/python/cpython/commit/3ddfa55)
- commit date: 2022-03-07T12:32:18+00:00
- ref: 3ddfa55df48a67a5972f

## linux x86_64

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-91-generic-x86_64-with-glibc2.31
- [raw results](bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55-vs-3.10.4.md)
- [plot](bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55-vs-3.10.4.png)

### vs. 3.11.0

- 1.06x slower \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55-vs-3.11.0.md)
- [plot](bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55-vs-3.11.0.png)

## darwin arm64

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55.json)

### vs. 3.10.4

- 1.17x faster
- missing benchmarks: mypy
- [table](bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55-vs-3.10.4.md)
- [plot](bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x slower
- missing benchmarks: mypy
- [table](bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55-vs-3.11.0.md)
- [plot](bm-20220307-darwin-arm64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55-vs-3.11.0.png)

