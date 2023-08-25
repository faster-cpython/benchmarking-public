# Results

- fork: brandtbucher
- version: 3.12.0a7+
- commit hash: [fd95518](https://github.com/brandtbucher/cpython/commit/fd95518)
- commit date: 2023-04-26T16:32:43-07:00
- commit merge base: [dc3f97549a8fe4f7fea8d0326e394760b51caa6e](https://github.com/brandtbucher/cpython/commit/dc3f97549a8fe4f7fea8d0326e394760b51caa6e)
- ref: immortal_interpreter

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4815929986)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-fd95518.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster \* (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-fd95518-vs-3.10.4.md)
- [plot](bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-fd95518-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x slower \* (HPT: reliability of 99.84%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-fd95518-vs-3.11.0.md)
- [plot](bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-fd95518-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 83.71%, 1.00x faster at 99th %ile)
- [table](bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-fd95518-vs-base.md)
- [plot](bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-fd95518-vs-base.png)

