# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [42f54d1](https://github.com/python/cpython/commit/42f54d1)
- commit date: 2023-05-06T18:53:48-04:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230506-azure-x86_64-python-main-3.12.0a7%2B-42f54d1-pystats.json)
- [pystats table](bm-20230506-azure-x86_64-python-main-3.12.0a7%2B-42f54d1-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4904372457)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230506-linux-x86_64-python-main-3.12.0a7%2B-42f54d1.json)

### vs. 3.10.4

- 1.25x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-linux-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md)
- [plot](bm-20230506-linux-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-linux-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md)
- [plot](bm-20230506-linux-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4904372457)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7%2B-42f54d1.json)

### vs. 3.10.4

- 1.27x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md)
- [plot](bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md)
- [plot](bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4904372457)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230506-pythonperf1-amd64-python-main-3.12.0a7%2B-42f54d1.json)

### vs. 3.10.4

- 1.16x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-pythonperf1-amd64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md)
- [plot](bm-20230506-pythonperf1-amd64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.png)

### vs. 3.11.0

- 1.05x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-pythonperf1-amd64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md)
- [plot](bm-20230506-pythonperf1-amd64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4904372457)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1.json)

### vs. 3.10.4

- 1.15x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.md)
- [plot](bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.10.4.png)

### vs. 3.11.0

- 1.05x slower
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.md)
- [plot](bm-20230506-darwin-arm64-python-main-3.12.0a7%2B-42f54d1-vs-3.11.0.png)

