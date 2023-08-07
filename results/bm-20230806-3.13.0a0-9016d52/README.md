# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [9016d52](https://github.com/brandtbucher/cpython/commit/9016d52)
- commit date: 2023-08-06T19:37:11-07:00
- commit merge base: [9564e31cbc95a723f2414537231bc4611b56644f](https://github.com/brandtbucher/cpython/commit/9564e31cbc95a723f2414537231bc4611b56644f)
- ref: uops_enabled

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5786875946)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52.json)

### vs. 3.10.4

- 1.20x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md)
- [plot](bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md)
- [plot](bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.png)

### vs. base

- 1.06x slower
- [table](bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md)
- [plot](bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5786875946)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52.json)

### vs. 3.10.4

- 1.07x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md)
- [plot](bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x slower
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md)
- [plot](bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.png)

### vs. base

- 1.03x slower
- [table](bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md)
- [plot](bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5786875946)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52.json)

### vs. 3.10.4

- 1.13x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.md)
- [plot](bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.10.4.png)

### vs. 3.11.0

- 1.07x slower
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.md)
- [plot](bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-3.11.0.png)

### vs. base

- 1.04x slower
- [table](bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.md)
- [plot](bm-20230806-darwin-arm64-brandtbucher-uops_enabled-3.13.0a0-9016d52-vs-base.png)

