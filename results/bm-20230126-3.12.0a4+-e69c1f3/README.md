# Results

- fork: gvanrossum
- version: 3.12.0a4+
- commit hash: [e69c1f3](https://github.com/gvanrossum/cpython/commit/e69c1f3)
- commit date: 2023-01-26T16:42:59-08:00
- commit merge base: [9f2c479eaf7d922746ef2f3c85b5c781757686b1](https://github.com/gvanrossum/cpython/commit/9f2c479eaf7d922746ef2f3c85b5c781757686b1)
- ref: e69c1f3e7a01d253e05b

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.10.4.md)
- [plot](bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.11.0.md)
- [plot](bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-base.md)
- [plot](bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-base.png)

## darwin arm64 (darwin)

- cpu model: missing
- platform: macOS-12.6-arm64-arm-64bit
- [raw results](bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3.json)

### vs. 3.10.4

- 1.23x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.10.4.md)
- [plot](bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: dask, mypy
- [table](bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.11.0.md)
- [plot](bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-base.md)
- [plot](bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4%2B-e69c1f3-vs-base.png)

