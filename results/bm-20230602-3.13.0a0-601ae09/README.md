# Results

- fork: python
- version: 3.13.0a0
- commit hash: [601ae09](https://github.com/python/cpython/commit/601ae09)
- commit date: 2023-06-02T10:39:38+01:00
- ref: 601ae09f0c8eda213b90

## linux x86_64 (azure)

- [pystats raw](bm-20230602-azure-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-pystats.json)
- [pystats table](bm-20230602-azure-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5583081209)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.10.4.md)
- [plot](bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 85.14%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.11.0.md)
- [plot](bm-20230602-linux-x86_64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5583081209)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.10.4.md)
- [plot](bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.11.0.md)
- [plot](bm-20230602-pythonperf1-amd64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5583081209)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.10.4.md)
- [plot](bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 58.85%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.11.0.md)
- [plot](bm-20230602-darwin-arm64-python-601ae09f0c8eda213b90-3.13.0a0-601ae09-vs-3.11.0.png)

