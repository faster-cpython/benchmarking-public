# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [f565bc6](https://github.com/brandtbucher/cpython/commit/f565bc6)
- commit date: 2023-08-05T09:07:05-07:00
- commit merge base: [aab6f7173a3b825599629dd6fa5cb7e477421595](https://github.com/brandtbucher/cpython/commit/aab6f7173a3b825599629dd6fa5cb7e477421595)
- ref: calls

## linux x86_64 (azure)

- [pystats raw](bm-20230805-azure-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-pystats.json)
- [pystats table](bm-20230805-azure-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-pystats.md)

### vs. base

- [pystats diff](bm-20230805-azure-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5801622663)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-3.10.4.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-3.11.0.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-base.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6-vs-base.png)

