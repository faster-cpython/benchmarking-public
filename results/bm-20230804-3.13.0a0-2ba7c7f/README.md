# Results

- fork: python
- version: 3.13.0a0
- commit hash: [2ba7c7f](https://github.com/python/cpython/commit/2ba7c7f)
- commit date: 2023-08-04T10:34:23+01:00
- ref: 2ba7c7f7b151ff56cf12

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5764235385)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f-vs-3.10.4.md)
- [plot](bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 72.22%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f-vs-3.11.0.md)
- [plot](bm-20230804-pythonperf2-x86_64-python-2ba7c7f7b151ff56cf12-3.13.0a0-2ba7c7f-vs-3.11.0.png)

