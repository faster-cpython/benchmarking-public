# Results

- fork: python
- version: 3.13.0a0
- commit hash: [af5cf1e](https://github.com/python/cpython/commit/af5cf1e)
- commit date: 2023-07-11T13:20:29+02:00
- ref: af5cf1e75136fcef967d

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5555057126)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.10.4.md)
- [plot](bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 74.05%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.11.0.md)
- [plot](bm-20230711-linux-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5544208185)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.10.4.md)
- [plot](bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 66.39%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.11.0.md)
- [plot](bm-20230711-pythonperf2-x86_64-python-af5cf1e75136fcef967d-3.13.0a0-af5cf1e-vs-3.11.0.png)

