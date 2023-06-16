# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [dbda923](https://github.com/brandtbucher/cpython/commit/dbda923)
- commit date: 2023-06-15T22:57:29-07:00
- commit merge base: [8f10140e74d141a0a894702044e213e6f0690d9c](https://github.com/brandtbucher/cpython/commit/8f10140e74d141a0a894702044e213e6f0690d9c)
- ref: clean_up_calls

## linux x86_64 (azure)

- [pystats raw](bm-20230615-azure-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-pystats.json)
- [pystats table](bm-20230615-azure-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5286724818)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-vs-3.10.4.md)
- [plot](bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-vs-3.11.0.md)
- [plot](bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-vs-base.md)
- [plot](bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923-vs-base.png)

