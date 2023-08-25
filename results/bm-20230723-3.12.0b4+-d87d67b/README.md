# Results

- fork: python
- version: 3.12.0b4+
- commit hash: [d87d67b](https://github.com/python/cpython/commit/d87d67b)
- commit date: 2023-07-23T00:01:44+00:00
- ref: 3.12

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5633523551)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230723-linux-x86_64-python-3.12-3.12.0b4%2B-d87d67b.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230723-linux-x86_64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.10.4.md)
- [plot](bm-20230723-linux-x86_64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 53.75%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230723-linux-x86_64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.11.0.md)
- [plot](bm-20230723-linux-x86_64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5633523551)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4%2B-d87d67b.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.10.4.md)
- [plot](bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.11.0.md)
- [plot](bm-20230723-pythonperf1-amd64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5633523551)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230723-darwin-arm64-python-3.12-3.12.0b4%2B-d87d67b.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230723-darwin-arm64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.10.4.md)
- [plot](bm-20230723-darwin-arm64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 74.11%, 1.00x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230723-darwin-arm64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.11.0.md)
- [plot](bm-20230723-darwin-arm64-python-3.12-3.12.0b4%2B-d87d67b-vs-3.11.0.png)

