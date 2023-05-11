# Results

- fork: python
- version: 3.12.0a6+
- commit hash: [f2e5a6e](https://github.com/python/cpython/commit/f2e5a6e)
- commit date: 2023-03-24T15:00:32+00:00
- ref: f2e5a6ee628502d307a9

## linux x86_64 (azure)

- [pystats raw](bm-20230324-azure-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6%2B-f2e5a6e-pystats.json)
- [pystats table](bm-20230324-azure-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6%2B-f2e5a6e-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4514597324)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6%2B-f2e5a6e.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6%2B-f2e5a6e-vs-3.10.4.md)
- [plot](bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6%2B-f2e5a6e-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6%2B-f2e5a6e-vs-3.11.0.md)
- [plot](bm-20230324-linux-x86_64-python-f2e5a6ee628502d307a9-3.12.0a6%2B-f2e5a6e-vs-3.11.0.png)

