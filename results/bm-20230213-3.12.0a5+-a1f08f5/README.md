# Results

- fork: python
- version: 3.12.0a5+
- commit hash: [a1f08f5](https://github.com/python/cpython/commit/a1f08f5)
- commit date: 2023-02-13T11:11:43+02:00
- ref: a1f08f5f19753c7c9295

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513538097)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230213-pythonperf2-x86_64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5.json)

### vs. 3.10.4

- 1.27x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230213-pythonperf2-x86_64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.10.4.md)
- [plot](bm-20230213-pythonperf2-x86_64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230213-pythonperf2-x86_64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.11.0.md)
- [plot](bm-20230213-pythonperf2-x86_64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610451007)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.10.4.md)
- [plot](bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.10.4.png)

### vs. 3.11.0

- 1.09x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.11.0.md)
- [plot](bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494505947)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230213-darwin-arm64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5.json)

### vs. 3.10.4

- 1.23x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230213-darwin-arm64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.10.4.md)
- [plot](bm-20230213-darwin-arm64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230213-darwin-arm64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.11.0.md)
- [plot](bm-20230213-darwin-arm64-python-a1f08f5f19753c7c9295-3.12.0a5%2B-a1f08f5-vs-3.11.0.png)

