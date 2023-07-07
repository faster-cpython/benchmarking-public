# Results

- fork: python
- version: 3.13.0a0
- commit hash: [e1d45b8](https://github.com/python/cpython/commit/e1d45b8)
- commit date: 2023-07-06T16:46:06-07:00
- ref: e1d45b8ed43e15908623

## linux x86_64 (azure)

- [pystats raw](bm-20230706-azure-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8-pystats.json)
- [pystats table](bm-20230706-azure-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5485259119)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8-vs-3.10.4.md)
- [plot](bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8-vs-3.11.0.md)
- [plot](bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8-vs-3.11.0.png)

