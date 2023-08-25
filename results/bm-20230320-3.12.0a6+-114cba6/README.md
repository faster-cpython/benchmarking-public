# Results

- fork: brandtbucher
- version: 3.12.0a6+
- commit hash: [114cba6](https://github.com/brandtbucher/cpython/commit/114cba6)
- commit date: 2023-03-20T10:55:44-07:00
- commit merge base: [5e6661bce968173fa45b74fa2111098645ff609c](https://github.com/brandtbucher/cpython/commit/5e6661bce968173fa45b74fa2111098645ff609c)
- ref: add_small_int_new

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4471382913)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-pystats.json)
- [pystats table](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-pystats.md)
- [raw results](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster \* (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-vs-3.10.4.md)
- [plot](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-vs-3.11.0.md)
- [plot](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 72.12%, 1.00x faster at 99th %ile)
- [table](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-vs-base.md)
- [plot](bm-20230320-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6%2B-114cba6-vs-base.png)

