# Results

- fork: iritkatriel
- version: 3.12.0a5+
- commit hash: [19b61a7](https://github.com/iritkatriel/cpython/commit/19b61a7)
- commit date: 2023-02-23T19:48:00+00:00
- commit merge base: [c3a178398c199038f3a0891d09f0363ec73f3b38](https://github.com/iritkatriel/cpython/commit/c3a178398c199038f3a0891d09f0363ec73f3b38)
- ref: fetch_restore

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4256286404)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster \* (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-3.10.4.md)
- [plot](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-3.11.0.md)
- [plot](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 98.99%, 1.00x slower at 99th %ile)
- [table](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-base.md)
- [plot](bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5%2B-19b61a7-vs-base.png)

