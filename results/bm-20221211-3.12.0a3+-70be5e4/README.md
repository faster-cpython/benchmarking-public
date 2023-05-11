# Results

- fork: python
- version: 3.12.0a3+
- commit hash: [70be5e4](https://github.com/python/cpython/commit/70be5e4)
- commit date: 2022-12-11T20:15:55-08:00
- ref: 70be5e42f6e288de32e0

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221211-linux-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4.json)

### vs. 3.10.4

- 1.31x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221211-linux-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.md)
- [plot](bm-20221211-linux-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221211-linux-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.md)
- [plot](bm-20221211-linux-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513537025)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4.json)

### vs. 3.10.4

- 1.25x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.md)
- [plot](bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.md)
- [plot](bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610450428)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4.json)

### vs. 3.10.4

- 1.17x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.md)
- [plot](bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.png)

### vs. 3.11.0

- 1.06x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.md)
- [plot](bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494504925)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4.json)

### vs. 3.10.4

- 1.21x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- [table](bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.md)
- [plot](bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.md)
- [plot](bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3%2B-70be5e4-vs-3.11.0.png)

