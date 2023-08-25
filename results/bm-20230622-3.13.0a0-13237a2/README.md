# Results

- fork: python
- version: 3.13.0a0
- commit hash: [13237a2](https://github.com/python/cpython/commit/13237a2)
- commit date: 2023-06-22T15:56:40+00:00
- ref: 13237a2da846efef9ce9

## linux x86_64 (azure)

- [pystats raw](bm-20230622-azure-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-pystats.json)
- [pystats table](bm-20230622-azure-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5350145818)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-vs-3.10.4.md)
- [plot](bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 94.01%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-vs-3.11.0.md)
- [plot](bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2-vs-3.11.0.png)

