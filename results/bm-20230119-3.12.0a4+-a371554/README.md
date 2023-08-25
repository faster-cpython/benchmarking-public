# Results

- fork: DinoV
- version: 3.12.0a4+
- commit hash: [a371554](https://github.com/DinoV/cpython/commit/a371554)
- commit date: 2023-01-19T14:42:31-08:00
- commit merge base: [a1e051a23736fdf3da812363bcaf32e53a294f03](https://github.com/DinoV/cpython/commit/a1e051a23736fdf3da812363bcaf32e53a294f03)
- ref: coro_freelist

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4%2B-a371554.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4%2B-a371554-vs-3.10.4.md)
- [plot](bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4%2B-a371554-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- new benchmarks: mypy
- [table](bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4%2B-a371554-vs-3.11.0.md)
- [plot](bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4%2B-a371554-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 95.99%, 1.00x faster at 99th %ile)
- [table](bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4%2B-a371554-vs-base.md)
- [plot](bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4%2B-a371554-vs-base.png)

