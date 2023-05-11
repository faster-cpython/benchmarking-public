# Results

- fork: python
- version: 3.12.0a6+
- commit hash: [e375bff](https://github.com/python/cpython/commit/e375bff)
- commit date: 2023-03-29T12:09:12+02:00
- ref: e375bff03736f809fbc2

## linux x86_64 (azure)

- [pystats raw](bm-20230329-azure-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-pystats.json)
- [pystats table](bm-20230329-azure-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4557316440)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-vs-3.10.4.md)
- [plot](bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-vs-3.11.0.md)
- [plot](bm-20230329-linux-x86_64-python-e375bff03736f809fbc2-3.12.0a6%2B-e375bff-vs-3.11.0.png)

