# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [ea2c001](https://github.com/python/cpython/commit/ea2c001)
- commit date: 2023-04-22T13:39:37-06:00
- ref: ea2c0016502472aa8baa

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4800546094)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001.json)

### vs. 3.10.4

- 1.24x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.10.4.md)
- [plot](bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.11.0.md)
- [plot](bm-20230422-linux-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4809383192)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001.json)

### vs. 3.10.4

- 1.26x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.10.4.md)
- [plot](bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.11.0.md)
- [plot](bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7%2B-ea2c001-vs-3.11.0.png)

