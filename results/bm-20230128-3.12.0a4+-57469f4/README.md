# Results

- fork: brandtbucher
- version: 3.12.0a4+
- commit hash: [57469f4](https://github.com/brandtbucher/cpython/commit/57469f4)
- commit date: 2023-01-28T09:58:59-08:00
- commit merge base: [8d18d1ffd52eb3917c4566b09596d596116a5532](https://github.com/brandtbucher/cpython/commit/8d18d1ffd52eb3917c4566b09596d596116a5532)
- ref: quicken_at_runtime

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-57469f4.json)

### vs. 3.10.4

- 1.29x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-57469f4-vs-3.10.4.md)
- [plot](bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-57469f4-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-57469f4-vs-3.11.0.md)
- [plot](bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-57469f4-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-57469f4-vs-base.md)
- [plot](bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-57469f4-vs-base.png)

