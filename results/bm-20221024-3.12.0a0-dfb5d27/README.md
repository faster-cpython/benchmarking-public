# Results

- fork: python
- version: 3.12.0a0
- commit hash: [dfb5d27](https://github.com/python/cpython/commit/dfb5d27)
- commit date: 2022-10-24T05:58:27-07:00
- ref: dfb5d272e6b99c2c70c6

## darwin arm64 (darwin)

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster \* (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27-vs-3.10.4.md)
- [plot](bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x slower \* (HPT: reliability of 98.96%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, flaskblogging, gc_traversal, gunicorn, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27-vs-3.11.0.md)
- [plot](bm-20221024-darwin-arm64-python-dfb5d272e6b99c2c70c6-3.12.0a0-dfb5d27-vs-3.11.0.png)

