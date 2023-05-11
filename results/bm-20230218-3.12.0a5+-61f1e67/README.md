# Results

- fork: python
- version: 3.12.0a5+
- commit hash: [61f1e67](https://github.com/python/cpython/commit/61f1e67)
- commit date: 2023-02-18T18:22:02-06:00
- ref: main

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4213724911)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-pystats.json)
- [pystats table](bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-pystats.md)
- [raw results](bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-vs-3.10.4.md)
- [plot](bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-vs-3.11.0.md)
- [plot](bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4213724911)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67.json)

### vs. 3.10.4

- 1.22x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.10.4.md)
- [plot](bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.11.0.md)
- [plot](bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.11.0.png)

