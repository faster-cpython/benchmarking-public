# Results

- fork: python
- version: 3.13.0a0
- commit hash: [80b9b3a](https://github.com/python/cpython/commit/80b9b3a)
- commit date: 2023-07-07T11:41:42-07:00
- ref: 80b9b3a51757ebb1e354

## linux x86_64 (azure)

- [pystats raw](bm-20230707-azure-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a-pystats.json)
- [pystats table](bm-20230707-azure-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5490292141)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a-vs-3.10.4.md)
- [plot](bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 53.22%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a-vs-3.11.0.md)
- [plot](bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a-vs-3.11.0.png)

