# Results

- fork: iritkatriel
- version: 3.12.0a4+
- commit hash: [2e2a861](https://github.com/iritkatriel/cpython/commit/2e2a861)
- commit date: 2023-02-06T19:01:48+00:00
- commit merge base: [c1b1f51cd1632f0b77dacd43092fb44ed5e053a9](https://github.com/iritkatriel/cpython/commit/c1b1f51cd1632f0b77dacd43092fb44ed5e053a9)
- ref: int_freelist

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-pystats.json)
- [pystats table](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-pystats.md)
- [raw results](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-vs-3.10.4.md)
- [plot](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-vs-3.11.0.md)
- [plot](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 55.98%, 1.00x faster at 99th %ile)
- [table](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-vs-base.md)
- [plot](bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4%2B-2e2a861-vs-base.png)

