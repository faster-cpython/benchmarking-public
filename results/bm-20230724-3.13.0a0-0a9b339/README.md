# Results

- fork: python
- version: 3.13.0a0
- commit hash: [0a9b339](https://github.com/python/cpython/commit/0a9b339)
- commit date: 2023-07-24T14:54:38+02:00
- ref: main

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5633523551)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339-vs-3.10.4.md)
- [plot](bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339-vs-3.11.0.md)
- [plot](bm-20230724-pythonperf2-x86_64-python-main-3.13.0a0-0a9b339-vs-3.11.0.png)

