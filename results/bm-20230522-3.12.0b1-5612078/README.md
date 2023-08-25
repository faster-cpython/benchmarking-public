# Results

- fork: python
- version: 3.12.0b1
- commit hash: [5612078](https://github.com/python/cpython/commit/5612078)
- commit date: 2023-05-22T14:07:36+02:00
- ref: v3.12.0b1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5246839304)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.md)
- [plot](bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 86.76%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.md)
- [plot](bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5246839304)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.md)
- [plot](bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.84%, 1.01x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.md)
- [plot](bm-20230522-pythonperf2-x86_64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5246839304)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.md)
- [plot](bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 62.59%, 1.00x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.md)
- [plot](bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5246839304)
- cpu model: missing
- platform: macOS-13.4-arm64-arm-64bit
- [raw results](bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.md)
- [plot](bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x faster (HPT: reliability of 64.10%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.md)
- [plot](bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078-vs-3.11.0.png)

