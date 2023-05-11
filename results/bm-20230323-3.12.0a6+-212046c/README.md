# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [212046c](https://github.com/brandtbucher/cpython/commit/212046c)
- commit date: 2023-03-23T11:27:23-07:00
- commit merge base: [87be8d95228ee95de9045cf2952311d20dc5de45](https://github.com/brandtbucher/cpython/commit/87be8d95228ee95de9045cf2952311d20dc5de45)
- ref: type_cache_fixed

## linux x86_64 (azure)

- [pystats raw](bm-20230323-azure-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-pystats.json)
- [pystats table](bm-20230323-azure-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4504214103)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-vs-3.10.4.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-vs-3.11.0.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-vs-3.11.0.png)

### vs. base

- 1.00x faster
- missing benchmarks: 🔴 sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-vs-base.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-212046c-vs-base.png)

