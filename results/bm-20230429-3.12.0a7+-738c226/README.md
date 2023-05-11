# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [738c226](https://github.com/python/cpython/commit/738c226)
- commit date: 2023-04-29T04:51:55+00:00
- ref: 738c226786997262b765

## linux x86_64 (azure)

- [pystats raw](bm-20230429-azure-x86_64-python-738c226786997262b765-3.12.0a7%2B-738c226-pystats.json)
- [pystats table](bm-20230429-azure-x86_64-python-738c226786997262b765-3.12.0a7%2B-738c226-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4837501205)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7%2B-738c226.json)

### vs. 3.10.4

- 1.24x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
- [table](bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7%2B-738c226-vs-3.10.4.md)
- [plot](bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7%2B-738c226-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols
- [table](bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7%2B-738c226-vs-3.11.0.md)
- [plot](bm-20230429-linux-x86_64-python-738c226786997262b765-3.12.0a7%2B-738c226-vs-3.11.0.png)

