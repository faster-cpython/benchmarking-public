# Results

- fork: mdboom
- version: 3.12.0a7+
- commit hash: [82b39b9](https://github.com/mdboom/cpython/commit/82b39b9)
- commit date: 2023-06-07T10:53:03-04:00
- commit merge base: [ea2c0016502472aa8baa3149050ada776d17a009](https://github.com/mdboom/cpython/commit/ea2c0016502472aa8baa3149050ada776d17a009)
- ref: match_nogil_immortal

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5202595165)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9.json)

### vs. 3.10.4

- 1.31x faster
- missing benchmarks: flaskblogging
- [table](bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-3.10.4.md)
- [plot](bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-3.10.4.png)

### vs. 3.11.0

- 1.05x faster
- missing benchmarks: flaskblogging
- [table](bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-3.11.0.md)
- [plot](bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-3.11.0.png)

### vs. base

- 1.04x faster \*
- new benchmarks: aiohttp, asyncio_tcp_ssl, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-base.md)
- [plot](bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7%2B-82b39b9-vs-base.png)

