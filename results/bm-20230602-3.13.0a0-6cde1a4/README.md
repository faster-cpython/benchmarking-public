# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [6cde1a4](https://github.com/faster%2dcpython/cpython/commit/6cde1a4)
- commit date: 2023-06-02T23:05:03+01:00
- commit merge base: [06893403668961fdbd5d9ece18162eb3470fc8dd](https://github.com/faster%2dcpython/cpython/commit/06893403668961fdbd5d9ece18162eb3470fc8dd)
- ref: remove_remaining_sup

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5176234839)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-3.10.4.md)
- [plot](bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-3.10.4.png)

### vs. 3.11.0

- 1.06x faster
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-3.11.0.md)
- [plot](bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-base.md)
- [plot](bm-20230602-pythonperf2-x86_64-faster%252dcpython-remove_remaining_sup-3.13.0a0-6cde1a4-vs-base.png)

