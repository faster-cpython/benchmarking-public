# Results

- fork: python
- version: 3.13.0a0
- commit hash: [3a314f7](https://github.com/python/cpython/commit/3a314f7)
- commit date: 2023-06-10T12:09:20-07:00
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20230610-azure-x86_64-python-main-3.13.0a0-3a314f7-pystats.json)
- [pystats table](bm-20230610-azure-x86_64-python-main-3.13.0a0-3a314f7-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5232692368)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7-vs-3.10.4.md)
- [plot](bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7-vs-3.11.0.md)
- [plot](bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5232692368)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7.json)

### vs. 3.10.4

- 1.31x faster
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7-vs-3.10.4.md)
- [plot](bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7-vs-3.10.4.png)

### vs. 3.11.0

- 1.08x faster
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7-vs-3.11.0.md)
- [plot](bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5232692368)
- cpu model: missing
- platform: macOS-13.4-arm64-arm-64bit
- [raw results](bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7.json)

### vs. 3.10.4

- 1.23x faster
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7-vs-3.10.4.md)
- [plot](bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7-vs-3.11.0.md)
- [plot](bm-20230610-darwin-arm64-python-main-3.13.0a0-3a314f7-vs-3.11.0.png)

