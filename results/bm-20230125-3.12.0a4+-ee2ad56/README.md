# Results

- fork: carljm
- version: 3.12.0a4+
- commit hash: [ee2ad56](https://github.com/carljm/cpython/commit/ee2ad56)
- commit date: 2023-01-25T00:55:36+00:00
- commit merge base: [f02fa64bf2d03ef7a28650c164e17a5fb5d8543d](https://github.com/carljm/cpython/commit/f02fa64bf2d03ef7a28650c164e17a5fb5d8543d)
- ref: inlinecomp

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4%2B-ee2ad56.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster \* (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4%2B-ee2ad56-vs-3.10.4.md)
- [plot](bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4%2B-ee2ad56-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4%2B-ee2ad56-vs-3.11.0.md)
- [plot](bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4%2B-ee2ad56-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 88.40%, 1.00x faster at 99th %ile)
- [table](bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4%2B-ee2ad56-vs-base.md)
- [plot](bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4%2B-ee2ad56-vs-base.png)

