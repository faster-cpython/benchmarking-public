# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [c87e8bd](https://github.com/brandtbucher/cpython/commit/c87e8bd)
- commit date: 2023-03-22T18:29:12-07:00
- commit merge base: [87be8d95228ee95de9045cf2952311d20dc5de45](https://github.com/brandtbucher/cpython/commit/87be8d95228ee95de9045cf2952311d20dc5de45)
- ref: type_cache

## linux x86_64 (azure)

- [pystats raw](bm-20230322-azure-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-pystats.json)
- [pystats table](bm-20230322-azure-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4497511965)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-vs-3.10.4.md)
- [plot](bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: comprehensions
- [table](bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-vs-3.11.0.md)
- [plot](bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-vs-3.11.0.png)

### vs. base

- 1.01x slower
- missing benchmarks: 🔴 aiohttp, coverage, djangocms, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-vs-base.md)
- [plot](bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-c87e8bd-vs-base.png)

