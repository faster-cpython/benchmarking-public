# Results

- fork: iritkatriel
- version: 3.12.0a4+
- commit hash: [1d81198](https://github.com/iritkatriel/cpython/commit/1d81198)
- commit date: 2023-02-03T15:14:21+00:00
- commit merge base: [c1b1f51cd1632f0b77dacd43092fb44ed5e053a9](https://github.com/iritkatriel/cpython/commit/c1b1f51cd1632f0b77dacd43092fb44ed5e053a9)
- ref: int_freelist

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-1d81198.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-1d81198-vs-3.10.4.md)
- [plot](bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-1d81198-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-1d81198-vs-3.11.0.md)
- [plot](bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-1d81198-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-1d81198-vs-base.md)
- [plot](bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-1d81198-vs-base.png)

