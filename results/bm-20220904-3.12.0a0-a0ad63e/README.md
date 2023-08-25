# Results

- fork: python
- version: 3.12.0a0
- commit hash: [a0ad63e](https://github.com/python/cpython/commit/a0ad63e)
- commit date: 2022-09-04T18:33:50-07:00
- ref: a0ad63e70e3682cdf7e8

## darwin arm64 (darwin)

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster \* (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e-vs-3.10.4.md)
- [plot](bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x faster \* (HPT: reliability of 51.69%, 1.00x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e-vs-3.11.0.md)
- [plot](bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e-vs-3.11.0.png)

