# Results

- fork: python
- version: 3.12.0a2+
- commit hash: [cdde29d](https://github.com/python/cpython/commit/cdde29d)
- commit date: 2022-11-21T10:50:20+01:00
- ref: cdde29dde90947df9bac

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d.json)

### vs. 3.10.4

- 1.32x faster \*
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.md)
- [plot](bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.md)
- [plot](bm-20221121-linux-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513536703)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d.json)

### vs. 3.10.4

- 1.24x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.md)
- [plot](bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.md)
- [plot](bm-20221121-pythonperf2-x86_64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4610450218)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d.json)

### vs. 3.10.4

- 1.19x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.md)
- [plot](bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.png)

### vs. 3.11.0

- 1.08x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.md)
- [plot](bm-20221121-pythonperf1-amd64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494504370)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d.json)

### vs. 3.10.4

- 1.18x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.md)
- [plot](bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.md)
- [plot](bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2%2B-cdde29d-vs-3.11.0.png)

