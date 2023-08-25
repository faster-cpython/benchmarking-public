# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [3516704](https://github.com/python/cpython/commit/3516704)
- commit date: 2023-04-08T10:56:42-07:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230408-azure-x86_64-python-main-3.12.0a7%2B-3516704-pystats.json)
- [pystats table](bm-20230408-azure-x86_64-python-main-3.12.0a7%2B-3516704-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4647840179)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230408-linux-x86_64-python-main-3.12.0a7%2B-3516704.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230408-linux-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md)
- [plot](bm-20230408-linux-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230408-linux-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md)
- [plot](bm-20230408-linux-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4647840179)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7%2B-3516704.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster \* (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md)
- [plot](bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md)
- [plot](bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4647840179)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230408-pythonperf1-amd64-python-main-3.12.0a7%2B-3516704.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster \* (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230408-pythonperf1-amd64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md)
- [plot](bm-20230408-pythonperf1-amd64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster \* (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230408-pythonperf1-amd64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md)
- [plot](bm-20230408-pythonperf1-amd64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4647840179)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230408-darwin-arm64-python-main-3.12.0a7%2B-3516704.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster \* (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230408-darwin-arm64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.md)
- [plot](bm-20230408-darwin-arm64-python-main-3.12.0a7%2B-3516704-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x slower \* (HPT: reliability of 98.69%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230408-darwin-arm64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.md)
- [plot](bm-20230408-darwin-arm64-python-main-3.12.0a7%2B-3516704-vs-3.11.0.png)

