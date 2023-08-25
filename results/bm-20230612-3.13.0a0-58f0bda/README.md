# Results

- fork: python
- version: 3.13.0a0
- commit hash: [58f0bda](https://github.com/python/cpython/commit/58f0bda)
- commit date: 2023-06-12T15:09:14+00:00
- ref: main

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5232692368)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda-vs-3.10.4.md)
- [plot](bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x faster (HPT: reliability of 98.47%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda-vs-3.11.0.md)
- [plot](bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda-vs-3.11.0.png)

