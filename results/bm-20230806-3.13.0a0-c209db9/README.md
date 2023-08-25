# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [c209db9](https://github.com/brandtbucher/cpython/commit/c209db9)
- commit date: 2023-08-06T14:18:37-07:00
- commit merge base: [9564e31cbc95a723f2414537231bc4611b56644f](https://github.com/brandtbucher/cpython/commit/9564e31cbc95a723f2414537231bc4611b56644f)
- ref: justin

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5779347737)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md)
- [plot](bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x faster (HPT: reliability of 99.33%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md)
- [plot](bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- [table](bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md)
- [plot](bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5779347737)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md)
- [plot](bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x slower (HPT: reliability of 97.23%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md)
- [plot](bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- [table](bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md)
- [plot](bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5779347737)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9.json)

### vs. 3.10.4

- Geometric mean: 1.08x faster (HPT: reliability of 99.93%, 1.02x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md)
- [plot](bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md)
- [plot](bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- [table](bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md)
- [plot](bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5779347737)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.md)
- [plot](bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.md)
- [plot](bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- [table](bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.md)
- [plot](bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9-vs-base.png)

