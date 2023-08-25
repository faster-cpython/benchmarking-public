# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [5d7d86f](https://github.com/python/cpython/commit/5d7d86f)
- commit date: 2023-04-07T12:11:11-07:00
- ref: 5d7d86f2fdbbfc23325e

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4669710692)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7%2B-5d7d86f.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster \* (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7%2B-5d7d86f-vs-3.10.4.md)
- [plot](bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7%2B-5d7d86f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7%2B-5d7d86f-vs-3.11.0.md)
- [plot](bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7%2B-5d7d86f-vs-3.11.0.png)

