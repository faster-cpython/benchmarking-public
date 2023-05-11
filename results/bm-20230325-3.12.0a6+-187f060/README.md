# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [187f060](https://github.com/brandtbucher/cpython/commit/187f060)
- commit date: 2023-03-25T10:18:36-07:00
- commit merge base: [e375bff03736f809fbc234010c087ef9d7e0d384](https://github.com/brandtbucher/cpython/commit/e375bff03736f809fbc234010c087ef9d7e0d384)
- ref: shrink_call

## linux x86_64 (azure)

- [pystats raw](bm-20230325-azure-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-pystats.json)
- [pystats table](bm-20230325-azure-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4557316440)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-vs-3.10.4.md)
- [plot](bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-vs-3.11.0.md)
- [plot](bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-vs-base.md)
- [plot](bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6%2B-187f060-vs-base.png)

