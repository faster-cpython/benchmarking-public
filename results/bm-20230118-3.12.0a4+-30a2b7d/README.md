# Results

- fork: brandtbucher
- version: 3.12.0a4+
- commit hash: [30a2b7d](https://github.com/brandtbucher/cpython/commit/30a2b7d)
- commit date: 2023-01-18T04:55:10-08:00
- commit merge base: [ea232716d3de1675478db3a302629ba43194c967](https://github.com/brandtbucher/cpython/commit/ea232716d3de1675478db3a302629ba43194c967)
- ref: quicken_at_runtime

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-30a2b7d.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-30a2b7d-vs-3.10.4.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-30a2b7d-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-30a2b7d-vs-3.11.0.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-30a2b7d-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-30a2b7d-vs-base.md)
- [plot](bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-30a2b7d-vs-base.png)

