# Results

- fork: faster-cpython
- version: 3.12.0a4+
- commit hash: [df06ef8](https://github.com/faster%2dcpython/cpython/commit/df06ef8)
- commit date: 2023-01-13T17:14:09+00:00
- commit merge base: [e5bd5ad70d9e549eeb80aadb4f3ccb0f2f23266d](https://github.com/faster%2dcpython/cpython/commit/e5bd5ad70d9e549eeb80aadb4f3ccb0f2f23266d)
- ref: fstring_with_intrins

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230113-linux-x86_64-faster%252dcpython-fstring_with_intrins-3.12.0a4%2B-df06ef8.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230113-linux-x86_64-faster%252dcpython-fstring_with_intrins-3.12.0a4%2B-df06ef8-vs-3.10.4.md)
- [plot](bm-20230113-linux-x86_64-faster%252dcpython-fstring_with_intrins-3.12.0a4%2B-df06ef8-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230113-linux-x86_64-faster%252dcpython-fstring_with_intrins-3.12.0a4%2B-df06ef8-vs-3.11.0.md)
- [plot](bm-20230113-linux-x86_64-faster%252dcpython-fstring_with_intrins-3.12.0a4%2B-df06ef8-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230113-linux-x86_64-faster%252dcpython-fstring_with_intrins-3.12.0a4%2B-df06ef8-vs-base.md)
- [plot](bm-20230113-linux-x86_64-faster%252dcpython-fstring_with_intrins-3.12.0a4%2B-df06ef8-vs-base.png)

