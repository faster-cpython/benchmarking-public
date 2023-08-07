# Results

- fork: python
- version: 3.13.0a0
- commit hash: [9564e31](https://github.com/python/cpython/commit/9564e31)
- commit date: 2023-08-06T13:58:00+00:00
- ref: 9564e31cbc95a723f241

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5786875946)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md)
- [plot](bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md)
- [plot](bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5786875946)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md)
- [plot](bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md)
- [plot](bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5786875946)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31.json)

### vs. 3.10.4

- 1.10x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md)
- [plot](bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md)
- [plot](bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5786875946)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31.json)

### vs. 3.10.4

- 1.18x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.md)
- [plot](bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x slower
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.md)
- [plot](bm-20230806-darwin-arm64-python-9564e31cbc95a723f241-3.13.0a0-9564e31-vs-3.11.0.png)

