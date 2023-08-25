# Results

- fork: itamaro
- version: 3.12.0a6+
- commit hash: [bcf40dc](https://github.com/itamaro/cpython/commit/bcf40dc)
- commit date: 2023-03-20T16:03:51-07:00
- commit merge base: [094cf392f49d3c16fe798863717f6c8e0f3734bb](https://github.com/itamaro/cpython/commit/094cf392f49d3c16fe798863717f6c8e0f3734bb)
- ref: eager_tasks_factory

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4475369618)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6%2B-bcf40dc.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6%2B-bcf40dc-vs-3.10.4.md)
- [plot](bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6%2B-bcf40dc-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6%2B-bcf40dc-vs-3.11.0.md)
- [plot](bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6%2B-bcf40dc-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 98.25%, 1.00x faster at 99th %ile)
- missing benchmarks: 🔴 tornado_http
- [table](bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6%2B-bcf40dc-vs-base.md)
- [plot](bm-20230320-linux-x86_64-itamaro-eager_tasks_factory-3.12.0a6%2B-bcf40dc-vs-base.png)

