# Results

- fork: python
- version: 3.12.0b3+
- commit hash: [9cd3664](https://github.com/python/cpython/commit/9cd3664)
- commit date: 2023-06-24T16:36:34-07:00
- ref: 3.12

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5366963137)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230624-linux-x86_64-python-3.12-3.12.0b3%2B-9cd3664.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230624-linux-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.md)
- [plot](bm-20230624-linux-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 59.27%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230624-linux-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.md)
- [plot](bm-20230624-linux-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5366963137)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3%2B-9cd3664.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.md)
- [plot](bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.md)
- [plot](bm-20230624-pythonperf2-x86_64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5366963137)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3%2B-9cd3664.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.md)
- [plot](bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 73.09%, 1.00x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.md)
- [plot](bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5366963137)
- cpu model: missing
- platform: macOS-13.4-arm64-arm-64bit
- [raw results](bm-20230624-darwin-arm64-python-3.12-3.12.0b3%2B-9cd3664.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230624-darwin-arm64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.md)
- [plot](bm-20230624-darwin-arm64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 59.69%, 1.00x faster at 99th %ile)
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- new benchmarks: dask
- [table](bm-20230624-darwin-arm64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.md)
- [plot](bm-20230624-darwin-arm64-python-3.12-3.12.0b3%2B-9cd3664-vs-3.11.0.png)

