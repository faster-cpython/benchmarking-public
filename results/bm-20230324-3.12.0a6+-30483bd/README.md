# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [30483bd](https://github.com/brandtbucher/cpython/commit/30483bd)
- commit date: 2023-03-24T01:53:14-07:00
- commit merge base: [87be8d95228ee95de9045cf2952311d20dc5de45](https://github.com/brandtbucher/cpython/commit/87be8d95228ee95de9045cf2952311d20dc5de45)
- ref: type_cache

## linux x86_64 (azure)

- [pystats raw](bm-20230324-azure-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-pystats.json)
- [pystats table](bm-20230324-azure-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4516051892)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-vs-3.10.4.md)
- [plot](bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-vs-3.11.0.md)
- [plot](bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-vs-3.11.0.png)

### vs. base

- 1.00x slower
- missing benchmarks: 🔴 aiohttp, coverage, djangocms, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-vs-base.md)
- [plot](bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6%2B-30483bd-vs-base.png)

