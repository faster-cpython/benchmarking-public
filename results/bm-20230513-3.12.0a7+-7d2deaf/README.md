# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [7d2deaf](https://github.com/python/cpython/commit/7d2deaf)
- commit date: 2023-05-13T13:45:36-07:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230513-azure-x86_64-python-main-3.12.0a7%2B-7d2deaf-pystats.json)
- [pystats table](bm-20230513-azure-x86_64-python-main-3.12.0a7%2B-7d2deaf-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4969605514)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230513-linux-x86_64-python-main-3.12.0a7%2B-7d2deaf.json)

### vs. 3.10.4

- 1.28x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230513-linux-x86_64-python-main-3.12.0a7%2B-7d2deaf-vs-3.10.4.md)
- [plot](bm-20230513-linux-x86_64-python-main-3.12.0a7%2B-7d2deaf-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230513-linux-x86_64-python-main-3.12.0a7%2B-7d2deaf-vs-3.11.0.md)
- [plot](bm-20230513-linux-x86_64-python-main-3.12.0a7%2B-7d2deaf-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4969605514)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230513-pythonperf1-amd64-python-main-3.12.0a7%2B-7d2deaf.json)

### vs. 3.10.4

- 1.19x faster
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230513-pythonperf1-amd64-python-main-3.12.0a7%2B-7d2deaf-vs-3.10.4.md)
- [plot](bm-20230513-pythonperf1-amd64-python-main-3.12.0a7%2B-7d2deaf-vs-3.10.4.png)

### vs. 3.11.0

- 1.06x faster
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230513-pythonperf1-amd64-python-main-3.12.0a7%2B-7d2deaf-vs-3.11.0.md)
- [plot](bm-20230513-pythonperf1-amd64-python-main-3.12.0a7%2B-7d2deaf-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4969605514)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230513-darwin-arm64-python-main-3.12.0a7%2B-7d2deaf.json)

### vs. 3.10.4

- 1.19x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230513-darwin-arm64-python-main-3.12.0a7%2B-7d2deaf-vs-3.10.4.md)
- [plot](bm-20230513-darwin-arm64-python-main-3.12.0a7%2B-7d2deaf-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230513-darwin-arm64-python-main-3.12.0a7%2B-7d2deaf-vs-3.11.0.md)
- [plot](bm-20230513-darwin-arm64-python-main-3.12.0a7%2B-7d2deaf-vs-3.11.0.png)

