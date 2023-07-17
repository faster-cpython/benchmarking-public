# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [a4921c7](https://github.com/brandtbucher/cpython/commit/a4921c7)
- commit date: 2023-07-16T21:08:35-07:00
- commit merge base: [601ae09f0c8eda213b9050892f5ce9b91f0aa522](https://github.com/brandtbucher/cpython/commit/601ae09f0c8eda213b9050892f5ce9b91f0aa522)
- ref: justin

## linux x86_64 (azure)

- [pystats raw](bm-20230716-azure-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-pystats.json)
- [pystats table](bm-20230716-azure-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-pystats.md)

### vs. base

- [pystats diff](bm-20230716-azure-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5577945745)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7.json)

### vs. 3.10.4

- 1.25x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.10.4.md)
- [plot](bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.11.0.md)
- [plot](bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.11.0.png)

### vs. base

- 1.02x slower
- [table](bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-vs-base.md)
- [plot](bm-20230716-linux-x86_64-brandtbucher-justin-3.13.0a0-a4921c7-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5577945745)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7.json)

### vs. 3.10.4

- 1.14x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.10.4.md)
- [plot](bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.11.0.md)
- [plot](bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.11.0.png)

### vs. base

- 1.04x slower
- [table](bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7-vs-base.md)
- [plot](bm-20230716-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-a4921c7-vs-base.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5577945745)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7.json)

### vs. 3.10.4

- 1.22x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.10.4.md)
- [plot](bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.11.0.md)
- [plot](bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7-vs-base.md)
- [plot](bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7-vs-base.png)

