# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [8b9f269](https://github.com/brandtbucher/cpython/commit/8b9f269)
- commit date: 2023-03-23T22:20:58-07:00
- commit merge base: [f2e5a6ee628502d307a97f587788d7022a200229](https://github.com/brandtbucher/cpython/commit/f2e5a6ee628502d307a97f587788d7022a200229)
- ref: shrink_binary_subscr

## linux x86_64 (azure)

- [pystats raw](bm-20230323-azure-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-pystats.json)
- [pystats table](bm-20230323-azure-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4515718480)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-vs-3.10.4.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-vs-3.11.0.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-vs-base.md)
- [plot](bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6%2B-8b9f269-vs-base.png)

