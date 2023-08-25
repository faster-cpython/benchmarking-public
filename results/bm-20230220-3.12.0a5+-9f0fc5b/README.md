# Results

- fork: carljm
- version: 3.12.0a5+
- commit hash: [9f0fc5b](https://github.com/carljm/cpython/commit/9f0fc5b)
- commit date: 2023-02-20T15:37:00-08:00
- commit merge base: [022b44f2546c44183e4df7b67e3e64502fae9143](https://github.com/carljm/cpython/commit/022b44f2546c44183e4df7b67e3e64502fae9143)
- ref: inlinecomp2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4252076033)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-9f0fc5b.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster \* (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-9f0fc5b-vs-3.10.4.md)
- [plot](bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-9f0fc5b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-9f0fc5b-vs-3.11.0.md)
- [plot](bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-9f0fc5b-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 97.02%, 1.00x faster at 99th %ile)
- [table](bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-9f0fc5b-vs-base.md)
- [plot](bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5%2B-9f0fc5b-vs-base.png)

