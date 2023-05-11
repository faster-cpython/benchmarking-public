# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [dff8e5d](https://github.com/python/cpython/commit/dff8e5d)
- commit date: 2023-04-27T16:54:59+08:00
- ref: dff8e5dc8d0758d1f9c5

## linux x86_64 (azure)

- [pystats raw](bm-20230427-azure-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7%2B-dff8e5d-pystats.json)
- [pystats table](bm-20230427-azure-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7%2B-dff8e5d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4823675939)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7%2B-dff8e5d.json)

### vs. 3.10.4

- 1.23x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn
- [table](bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7%2B-dff8e5d-vs-3.10.4.md)
- [plot](bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7%2B-dff8e5d-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7%2B-dff8e5d-vs-3.11.0.md)
- [plot](bm-20230427-linux-x86_64-python-dff8e5dc8d0758d1f9c5-3.12.0a7%2B-dff8e5d-vs-3.11.0.png)

