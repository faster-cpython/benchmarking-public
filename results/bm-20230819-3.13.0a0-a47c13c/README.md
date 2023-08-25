# Results

- fork: python
- version: 3.13.0a0
- commit hash: [a47c13c](https://github.com/python/cpython/commit/a47c13c)
- commit date: 2023-08-19T13:14:38-07:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230819-azure-x86_64-python-main-3.13.0a0-a47c13c-pystats.json)
- [pystats table](bm-20230819-azure-x86_64-python-main-3.13.0a0-a47c13c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5914309107)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c-vs-3.10.4.md)
- [plot](bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 82.54%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c-vs-3.11.0.md)
- [plot](bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5914309107)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c-vs-3.10.4.md)
- [plot](bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 94.74%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c-vs-3.11.0.md)
- [plot](bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5914309107)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c-vs-3.10.4.md)
- [plot](bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 56.88%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c-vs-3.11.0.md)
- [plot](bm-20230819-pythonperf1-amd64-python-main-3.13.0a0-a47c13c-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5914309107)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c-vs-3.10.4.md)
- [plot](bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.24%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c-vs-3.11.0.md)
- [plot](bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c-vs-3.11.0.png)

