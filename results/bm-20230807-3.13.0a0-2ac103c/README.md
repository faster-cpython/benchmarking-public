# Results

- fork: python
- version: 3.13.0a0
- commit hash: [2ac103c](https://github.com/python/cpython/commit/2ac103c)
- commit date: 2023-08-07T13:46:36+01:00
- ref: 2ac103c346ffe9d0e4c1

## linux x86_64 (azure)

- [pystats raw](bm-20230807-azure-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-pystats.json)
- [pystats table](bm-20230807-azure-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5878234093)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.10.4.md)
- [plot](bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 74.05%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.11.0.md)
- [plot](bm-20230807-linux-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5796074095)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.10.4.md)
- [plot](bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 76.53%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.11.0.md)
- [plot](bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c-vs-3.11.0.png)

