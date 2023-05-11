# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [b201b6d](https://github.com/brandtbucher/cpython/commit/b201b6d)
- commit date: 2023-03-24T02:39:55-07:00
- commit merge base: [f2e5a6ee628502d307a97f587788d7022a200229](https://github.com/brandtbucher/cpython/commit/f2e5a6ee628502d307a97f587788d7022a200229)
- ref: quicken_at_runtime_n

## linux x86_64 (azure)

- [pystats raw](bm-20230324-azure-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-pystats.json)
- [pystats table](bm-20230324-azure-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4516271878)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-vs-3.10.4.md)
- [plot](bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-vs-3.11.0.md)
- [plot](bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-vs-base.md)
- [plot](bm-20230324-linux-x86_64-brandtbucher-quicken_at_runtime_n-3.12.0a6%2B-b201b6d-vs-base.png)

