# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [0e21f47](https://github.com/brandtbucher/cpython/commit/0e21f47)
- commit date: 2023-03-23T04:15:02-07:00
- commit merge base: [87be8d95228ee95de9045cf2952311d20dc5de45](https://github.com/brandtbucher/cpython/commit/87be8d95228ee95de9045cf2952311d20dc5de45)
- ref: type_cache

## linux x86_64 (azure)

- [pystats raw](bm-20230323-azure-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-pystats.json)
- [pystats table](bm-20230323-azure-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4501963712)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-vs-3.10.4.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster
- missing benchmarks: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-vs-3.11.0.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-vs-3.11.0.png)

### vs. base

- 1.01x slower
- missing benchmarks: 🔴 aiohttp, coverage, djangocms, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-vs-base.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-0e21f47-vs-base.png)

