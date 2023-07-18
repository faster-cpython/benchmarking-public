# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [ba47232](https://github.com/brandtbucher/cpython/commit/ba47232)
- commit date: 2023-07-17T17:37:04-07:00
- commit merge base: [601ae09f0c8eda213b9050892f5ce9b91f0aa522](https://github.com/brandtbucher/cpython/commit/601ae09f0c8eda213b9050892f5ce9b91f0aa522)
- ref: justin

## linux x86_64 (azure)

- [pystats raw](bm-20230717-azure-x86_64-brandtbucher-justin-3.13.0a0-ba47232-pystats.json)
- [pystats table](bm-20230717-azure-x86_64-brandtbucher-justin-3.13.0a0-ba47232-pystats.md)

### vs. base

- [pystats diff](bm-20230717-azure-x86_64-brandtbucher-justin-3.13.0a0-ba47232-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5583081209)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.md)
- [plot](bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.md)
- [plot](bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.md)
- [plot](bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5583081209)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232.json)

### vs. 3.10.4

- 1.16x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.md)
- [plot](bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.md)
- [plot](bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.png)

### vs. base

- 1.03x slower
- [table](bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.md)
- [plot](bm-20230717-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5583081209)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232.json)

### vs. 3.10.4

- 1.21x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.md)
- [plot](bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.md)
- [plot](bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-3.11.0.png)

### vs. base

- 1.02x slower
- [table](bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.md)
- [plot](bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232-vs-base.png)

