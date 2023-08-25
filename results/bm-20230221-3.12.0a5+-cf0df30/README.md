# Results

- fork: brandtbucher
- version: 3.12.0a5+
- commit hash: [cf0df30](https://github.com/brandtbucher/cpython/commit/cf0df30)
- commit date: 2023-02-21T11:24:49-08:00
- commit merge base: [d5c7954d0c3ff874d2d27d33dcc207bb7356f328](https://github.com/brandtbucher/cpython/commit/d5c7954d0c3ff874d2d27d33dcc207bb7356f328)
- ref: shrink_load_global

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4236157262)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-pystats.json)
- [pystats table](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-pystats.md)
- [raw results](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-3.10.4.md)
- [plot](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-3.11.0.md)
- [plot](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 58.12%, 1.00x slower at 99th %ile)
- [table](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-base.md)
- [plot](bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5%2B-cf0df30-vs-base.png)

