# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [da1980a](https://github.com/python/cpython/commit/da1980a)
- commit date: 2023-05-03T17:28:44+01:00
- ref: da1980afcb8820ffaa05

## linux x86_64 (azure)

- [pystats raw](bm-20230503-azure-x86_64-python-da1980afcb8820ffaa05-3.12.0a7%2B-da1980a-pystats.json)
- [pystats table](bm-20230503-azure-x86_64-python-da1980afcb8820ffaa05-3.12.0a7%2B-da1980a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4879039553)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7%2B-da1980a.json)

### vs. 3.10.4

- 1.24x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7%2B-da1980a-vs-3.10.4.md)
- [plot](bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7%2B-da1980a-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7%2B-da1980a-vs-3.11.0.md)
- [plot](bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7%2B-da1980a-vs-3.11.0.png)

