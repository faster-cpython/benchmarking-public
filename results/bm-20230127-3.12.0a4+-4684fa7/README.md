# Results

- fork: iritkatriel
- version: 3.12.0a4+
- commit hash: [4684fa7](https://github.com/iritkatriel/cpython/commit/4684fa7)
- commit date: 2023-01-27T18:23:20+00:00
- commit merge base: [409f5337a3e466a5ef673797575cbd1745d27ca9](https://github.com/iritkatriel/cpython/commit/409f5337a3e466a5ef673797575cbd1745d27ca9)
- ref: single_op_exit

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4%2B-4684fa7.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4%2B-4684fa7-vs-3.10.4.md)
- [plot](bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4%2B-4684fa7-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4%2B-4684fa7-vs-3.11.0.md)
- [plot](bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4%2B-4684fa7-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4%2B-4684fa7-vs-base.md)
- [plot](bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4%2B-4684fa7-vs-base.png)

