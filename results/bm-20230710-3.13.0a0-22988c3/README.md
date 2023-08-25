# Results

- fork: python
- version: 3.13.0a0
- commit hash: [22988c3](https://github.com/python/cpython/commit/22988c3)
- commit date: 2023-07-10T16:04:26-07:00
- ref: 22988c323ad621b9f47b

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5517779334)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.10.4.md)
- [plot](bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 65.37%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.11.0.md)
- [plot](bm-20230710-pythonperf2-x86_64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5517797991)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.10.4.md)
- [plot](bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x faster (HPT: reliability of 89.94%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.11.0.md)
- [plot](bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3-vs-3.11.0.png)

