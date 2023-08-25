# Results

- fork: python
- version: 3.13.0a0
- commit hash: [8571b27](https://github.com/python/cpython/commit/8571b27)
- commit date: 2023-07-02T01:39:38+00:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230702-azure-x86_64-python-main-3.13.0a0-8571b27-pystats.json)
- [pystats table](bm-20230702-azure-x86_64-python-main-3.13.0a0-8571b27-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5433854694)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27-vs-3.10.4.md)
- [plot](bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 63.12%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27-vs-3.11.0.md)
- [plot](bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27-vs-3.11.0.png)

