# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [806df38](https://github.com/brandtbucher/cpython/commit/806df38)
- commit date: 2023-07-10T16:20:36-07:00
- commit merge base: [a840806d338805fe74a9de01081d30da7605a29f](https://github.com/brandtbucher/cpython/commit/a840806d338805fe74a9de01081d30da7605a29f)
- ref: not_none

## linux x86_64 (azure)

- [pystats raw](bm-20230710-azure-x86_64-brandtbucher-not_none-3.13.0a0-806df38-pystats.json)
- [pystats table](bm-20230710-azure-x86_64-brandtbucher-not_none-3.13.0a0-806df38-pystats.md)

### vs. base

- [pystats diff](bm-20230710-azure-x86_64-brandtbucher-not_none-3.13.0a0-806df38-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5514179612)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38-vs-3.10.4.md)
- [plot](bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38-vs-3.11.0.md)
- [plot](bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38-vs-base.md)
- [plot](bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38-vs-base.png)

