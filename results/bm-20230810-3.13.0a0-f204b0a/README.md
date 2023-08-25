# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [f204b0a](https://github.com/faster%2dcpython/cpython/commit/f204b0a)
- commit date: 2023-08-10T07:47:12+01:00
- commit merge base: [37d8b904f8b5b660f556597b21c0933b841d18de](https://github.com/faster%2dcpython/cpython/commit/37d8b904f8b5b660f556597b21c0933b841d18de)
- ref: no_untrack_dicts

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5834176363)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230810-pythonperf2-x86_64-faster%252dcpython-no_untrack_dicts-3.13.0a0-f204b0a.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230810-pythonperf2-x86_64-faster%252dcpython-no_untrack_dicts-3.13.0a0-f204b0a-vs-3.10.4.md)
- [plot](bm-20230810-pythonperf2-x86_64-faster%252dcpython-no_untrack_dicts-3.13.0a0-f204b0a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 88.21%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230810-pythonperf2-x86_64-faster%252dcpython-no_untrack_dicts-3.13.0a0-f204b0a-vs-3.11.0.md)
- [plot](bm-20230810-pythonperf2-x86_64-faster%252dcpython-no_untrack_dicts-3.13.0a0-f204b0a-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 96.99%, 1.00x faster at 99th %ile)
- [table](bm-20230810-pythonperf2-x86_64-faster%252dcpython-no_untrack_dicts-3.13.0a0-f204b0a-vs-base.md)
- [plot](bm-20230810-pythonperf2-x86_64-faster%252dcpython-no_untrack_dicts-3.13.0a0-f204b0a-vs-base.png)

