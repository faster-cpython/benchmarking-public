# Results

- fork: python
- version: 3.12.0a6+
- commit hash: [3adb23a](https://github.com/python/cpython/commit/3adb23a)
- commit date: 2023-03-18T12:21:48-05:00
- ref: main

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4458052230)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-pystats.json)
- [pystats table](bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-pystats.md)
- [raw results](bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster \* (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-vs-3.10.4.md)
- [plot](bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-vs-3.11.0.md)
- [plot](bm-20230318-linux-x86_64-python-main-3.12.0a6%2B-3adb23a-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4458052230)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster \* (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.10.4.md)
- [plot](bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x slower \* (HPT: reliability of 94.24%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.11.0.md)
- [plot](bm-20230318-darwin-arm64-python-main-3.12.0a6%2B-3adb23a-vs-3.11.0.png)

