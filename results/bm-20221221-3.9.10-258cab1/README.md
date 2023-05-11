# Results

- fork: faster_cpython
- version: 3.9.10
- commit hash: [258cab1](https://github.com/faster_cpython/cpython/commit/258cab1)
- commit date: 2022-12-21T19:44:41-08:00
- ref: nogil

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1.json)

### vs. 3.10.4

- 1.01x faster \*
- missing benchmarks: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1-vs-3.10.4.md)
- [plot](bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1-vs-3.10.4.png)

### vs. 3.11.0

- 1.25x slower \*
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2, pprint_safe_repr, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1-vs-3.11.0.md)
- [plot](bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1-vs-3.11.0.png)

