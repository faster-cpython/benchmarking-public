# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [f5c3838](https://github.com/python/cpython/commit/f5c3838)
- commit date: 2023-05-04T17:45:56+00:00
- ref: f5c38382f9c40f0017ce

## linux x86_64 (azure)

- [pystats raw](bm-20230504-azure-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7%2B-f5c3838-pystats.json)
- [pystats table](bm-20230504-azure-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7%2B-f5c3838-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4885872441)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7%2B-f5c3838.json)

### vs. 3.10.4

- 1.23x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7%2B-f5c3838-vs-3.10.4.md)
- [plot](bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7%2B-f5c3838-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7%2B-f5c3838-vs-3.11.0.md)
- [plot](bm-20230504-linux-x86_64-python-f5c38382f9c40f0017ce-3.12.0a7%2B-f5c3838-vs-3.11.0.png)

