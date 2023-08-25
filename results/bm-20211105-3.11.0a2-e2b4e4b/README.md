# Results

- fork: python
- version: 3.11.0a2
- commit hash: [e2b4e4b](https://github.com/python/cpython/commit/e2b4e4b)
- commit date: 2021-11-05T19:04:04+00:00
- ref: e2b4e4bab90b69fbd361

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster \* (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.md)
- [plot](bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x slower \* (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.md)
- [plot](bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4513535196)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster \* (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.md)
- [plot](bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x slower \* (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.md)
- [plot](bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4491158300)
- cpu model: missing
- platform: Windows-10-10.0.22000
- [raw results](bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b.json)

### vs. 3.10.4

- Geometric mean: 1.03x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.md)
- [plot](bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x slower \* (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.md)
- [plot](bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4494503166)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster \* (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.md)
- [plot](bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x slower \* (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.md)
- [plot](bm-20211105-darwin-arm64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b-vs-3.11.0.png)

