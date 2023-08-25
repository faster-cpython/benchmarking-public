# Results

- fork: iritkatriel
- version: 3.12.0a5+
- commit hash: [d83af14](https://github.com/iritkatriel/cpython/commit/d83af14)
- commit date: 2023-02-23T16:42:26+00:00
- commit merge base: [c3a178398c199038f3a0891d09f0363ec73f3b38](https://github.com/iritkatriel/cpython/commit/c3a178398c199038f3a0891d09f0363ec73f3b38)
- ref: fetch_restore

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4254873871)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-3.10.4.md)
- [plot](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-3.11.0.md)
- [plot](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- [table](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-base.md)
- [plot](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-d83af14-vs-base.png)

