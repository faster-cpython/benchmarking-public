# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [2cd1c87](https://github.com/python/cpython/commit/2cd1c87)
- commit date: 2023-05-14T21:05:35+00:00
- ref: main

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4969605514)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7%2B-2cd1c87.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7%2B-2cd1c87-vs-3.10.4.md)
- [plot](bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7%2B-2cd1c87-vs-3.10.4.png)

### vs. 3.11.0

- 1.07x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7%2B-2cd1c87-vs-3.11.0.md)
- [plot](bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7%2B-2cd1c87-vs-3.11.0.png)

