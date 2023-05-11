# Results

- fork: brandtbucher
- version: 3.12.0a4+
- commit hash: [fa5965d](https://github.com/brandtbucher/cpython/commit/fa5965d)
- commit date: 2023-02-02T04:49:07-08:00
- commit merge base: [5dcae3f0c3e9072251217e814a9438670e5f1e40](https://github.com/brandtbucher/cpython/commit/5dcae3f0c3e9072251217e814a9438670e5f1e40)
- ref: quicken_at_runtime

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-pystats.json)
- [pystats table](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-pystats.md)
- [raw results](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: comprehensions, flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: mypy
- [table](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-vs-3.10.4.md)
- [plot](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-vs-3.11.0.md)
- [plot](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-vs-base.md)
- [plot](bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4%2B-fa5965d-vs-base.png)

