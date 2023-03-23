# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [bde6bec](https://github.com/brandtbucher/cpython/commit/bde6bec)
- commit date: 2023-03-23T04:35:15-07:00
- commit merge base: [87be8d95228ee95de9045cf2952311d20dc5de45](https://github.com/brandtbucher/cpython/commit/87be8d95228ee95de9045cf2952311d20dc5de45)
- ref: type_cache_fixed

## linux x86_64 (azure)

- [pystats raw](bm-20230323-azure-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-pystats.json)
- [pystats table](bm-20230323-azure-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4502137017)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec.json)

### vs. 3.10.4

- 1.29x faster \*
- missing benchmarks: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: comprehensions
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-vs-3.10.4.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: comprehensions
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-vs-3.11.0.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-vs-3.11.0.png)

### vs. base

- 1.01x slower
- missing benchmarks: 🔴 aiohttp, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-vs-base.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6%2B-bde6bec-vs-base.png)

