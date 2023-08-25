# Results

- fork: python
- version: 3.12.0b4+
- commit hash: [30c127f](https://github.com/python/cpython/commit/30c127f)
- commit date: 2023-07-15T22:43:46+00:00
- ref: 3.12

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5564954493)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230715-linux-x86_64-python-3.12-3.12.0b4%2B-30c127f.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-linux-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.md)
- [plot](bm-20230715-linux-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 82.07%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-linux-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.md)
- [plot](bm-20230715-linux-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5564954493)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4%2B-30c127f.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.md)
- [plot](bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.70%, 1.00x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.md)
- [plot](bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5564954493)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4%2B-30c127f.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.md)
- [plot](bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.md)
- [plot](bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5564954493)
- cpu model: missing
- platform: macOS-13.4.1-arm64-arm-64bit
- [raw results](bm-20230715-darwin-arm64-python-3.12-3.12.0b4%2B-30c127f.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-darwin-arm64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.md)
- [plot](bm-20230715-darwin-arm64-python-3.12-3.12.0b4%2B-30c127f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 77.98%, 1.00x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230715-darwin-arm64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.md)
- [plot](bm-20230715-darwin-arm64-python-3.12-3.12.0b4%2B-30c127f-vs-3.11.0.png)

