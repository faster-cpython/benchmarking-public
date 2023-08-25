# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [affedee](https://github.com/python/cpython/commit/affedee)
- commit date: 2023-04-06T20:17:53+01:00
- ref: affedee8bf2ec00c404f

## linux x86_64 (azure)

- [pystats raw](bm-20230406-azure-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-pystats.json)
- [pystats table](bm-20230406-azure-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4633367492)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.10.4.md)
- [plot](bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.11.0.md)
- [plot](bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7%2B-affedee-vs-3.11.0.png)

