# Results

- fork: python
- version: 3.12.0a7+
- commit hash: [99b6418](https://github.com/python/cpython/commit/99b6418)
- commit date: 2023-05-21T01:19:56+01:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230521-azure-x86_64-python-main-3.12.0a7%2B-99b6418-pystats.json)
- [pystats table](bm-20230521-azure-x86_64-python-main-3.12.0a7%2B-99b6418-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5034892208)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230521-linux-x86_64-python-main-3.12.0a7%2B-99b6418.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230521-linux-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md)
- [plot](bm-20230521-linux-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 84.58%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230521-linux-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md)
- [plot](bm-20230521-linux-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5034892208)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7%2B-99b6418.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md)
- [plot](bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md)
- [plot](bm-20230521-pythonperf2-x86_64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5034892208)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md)
- [plot](bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md)
- [plot](bm-20230521-pythonperf1-amd64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5034892208)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.md)
- [plot](bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.md)
- [plot](bm-20230521-darwin-arm64-python-main-3.12.0a7%2B-99b6418-vs-3.11.0.png)

