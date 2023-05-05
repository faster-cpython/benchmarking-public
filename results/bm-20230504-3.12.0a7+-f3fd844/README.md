# Results

- fork: ericsnowcurrently
- version: 3.12.0a7+
- commit hash: [f3fd844](https://github.com/ericsnowcurrently/cpython/commit/f3fd844)
- commit date: 2023-05-04T17:46:15-06:00
- commit merge base: [e95dd40aff35775efce4c03bec7d82f03711310b](https://github.com/ericsnowcurrently/cpython/commit/e95dd40aff35775efce4c03bec7d82f03711310b)
- ref: per_interpreter_gil_

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4888788329)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844.json)

### vs. 3.10.4

- 1.23x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.md)
- [plot](bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.md)
- [plot](bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.md)
- [plot](bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4888788329)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844.json)

### vs. 3.10.4

- 1.27x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.md)
- [plot](bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.md)
- [plot](bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.md)
- [plot](bm-20230504-pythonperf2-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4888788329)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844.json)

### vs. 3.10.4

- 1.15x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.md)
- [plot](bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.md)
- [plot](bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.md)
- [plot](bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4888788329)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844.json)

### vs. 3.10.4

- 1.15x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.md)
- [plot](bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.10.4.png)

### vs. 3.11.0

- 1.05x slower
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.md)
- [plot](bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.md)
- [plot](bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-f3fd844-vs-base.png)

