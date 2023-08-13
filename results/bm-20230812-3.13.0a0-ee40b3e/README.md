# Results

- fork: python
- version: 3.13.0a0
- commit hash: [ee40b3e](https://github.com/python/cpython/commit/ee40b3e)
- commit date: 2023-08-12T23:46:00+00:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230812-azure-x86_64-python-main-3.13.0a0-ee40b3e-pystats.json)
- [pystats table](bm-20230812-azure-x86_64-python-main-3.13.0a0-ee40b3e-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5844242076)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.md)
- [plot](bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.md)
- [plot](bm-20230812-linux-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5844242076)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.md)
- [plot](bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.md)
- [plot](bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5844242076)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e.json)

### vs. 3.10.4

- 1.13x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.md)
- [plot](bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.md)
- [plot](bm-20230812-pythonperf1-amd64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5844242076)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e.json)

### vs. 3.10.4

- 1.20x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.md)
- [plot](bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.md)
- [plot](bm-20230812-darwin-arm64-python-main-3.13.0a0-ee40b3e-vs-3.11.0.png)

