# Results

- fork: brandtbucher
- version: 3.12.0a4+
- commit hash: [afbac86](https://github.com/brandtbucher/cpython/commit/afbac86)
- commit date: 2023-01-17T05:32:49-08:00
- commit merge base: [8d18d1ffd52eb3917c4566b09596d596116a5532](https://github.com/brandtbucher/cpython/commit/8d18d1ffd52eb3917c4566b09596d596116a5532)
- ref: quicken_in_compiler

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-pystats.json)
- [pystats table](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-pystats.md)
- [raw results](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster \* (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-vs-3.10.4.md)
- [plot](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-vs-3.11.0.md)
- [plot](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 97.23%, 1.00x slower at 99th %ile)
- [table](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-vs-base.md)
- [plot](bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4%2B-afbac86-vs-base.png)

