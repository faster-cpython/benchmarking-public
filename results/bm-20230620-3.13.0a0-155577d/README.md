# Results

- fork: python
- version: 3.13.0a0
- commit hash: [155577d](https://github.com/python/cpython/commit/155577d)
- commit date: 2023-06-20T10:12:44+02:00
- ref: 155577de1b6a7f4404b2

## linux x86_64 (azure)

- [pystats raw](bm-20230620-azure-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-pystats.json)
- [pystats table](bm-20230620-azure-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5333116681)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-vs-3.10.4.md)
- [plot](bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.67%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-vs-3.11.0.md)
- [plot](bm-20230620-pythonperf2-x86_64-python-155577de1b6a7f4404b2-3.13.0a0-155577d-vs-3.11.0.png)

