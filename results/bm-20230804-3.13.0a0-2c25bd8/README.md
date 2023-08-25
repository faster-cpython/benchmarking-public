# Results

- fork: python
- version: 3.13.0a0
- commit hash: [2c25bd8](https://github.com/python/cpython/commit/2c25bd8)
- commit date: 2023-08-04T20:41:04+01:00
- ref: 2c25bd82f46df72c89ca

## linux x86_64 (azure)

- [pystats raw](bm-20230804-azure-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-pystats.json)
- [pystats table](bm-20230804-azure-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5767335165)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-vs-3.10.4.md)
- [plot](bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 92.38%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-vs-3.11.0.md)
- [plot](bm-20230804-linux-x86_64-python-2c25bd82f46df72c89ca-3.13.0a0-2c25bd8-vs-3.11.0.png)

