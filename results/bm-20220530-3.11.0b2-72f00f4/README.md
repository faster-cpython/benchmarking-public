# Results

- fork: python
- version: 3.11.0b2
- commit hash: [72f00f4](https://github.com/python/cpython/commit/72f00f4)
- commit date: 2022-05-30T22:18:15+01:00
- commit date: 2022-05-30T21:18:15+00:00
- ref: 72f00f420afaba3bc873, main

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-91-generic-x86_64-with-glibc2.31
- [raw results](bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4-vs-3.10.4.md)
- [plot](bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- [table](bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4-vs-3.11.0.md)
- [plot](bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4483411222)
- cpu model: missing
- platform: Windows-10-10.0.22000-SP0
- [raw results](bm-20220530-pythonperf1-amd64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4.json)

### vs. 3.10.4

- 1.09x faster
- missing benchmarks: flaskblogging
- [table](bm-20220530-pythonperf1-amd64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.10.4.md)
- [plot](bm-20220530-pythonperf1-amd64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower
- missing benchmarks: flaskblogging
- [table](bm-20220530-pythonperf1-amd64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.11.0.md)
- [plot](bm-20220530-pythonperf1-amd64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.11.0.png)

## darwin arm64 (darwin)

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4.json)

### vs. 3.10.4

- 1.22x faster \*
- missing benchmarks: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, flaskblogging, gc_traversal, mypy2
- new benchmarks: mypy
- [table](bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.10.4.md)
- [plot](bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster \*
- missing benchmarks: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, flaskblogging, gc_traversal, mypy2
- new benchmarks: mypy
- [table](bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.11.0.md)
- [plot](bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4-vs-3.11.0.png)

