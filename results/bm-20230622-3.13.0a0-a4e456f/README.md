# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [a4e456f](https://github.com/brandtbucher/cpython/commit/a4e456f)
- commit date: 2023-06-22T13:41:50-07:00
- commit merge base: [13237a2da846efef9ce9b93fd4bcfebd49933568](https://github.com/brandtbucher/cpython/commit/13237a2da846efef9ce9b93fd4bcfebd49933568)
- ref: un_materialize

## linux x86_64 (azure)

- [pystats raw](bm-20230622-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-pystats.json)
- [pystats table](bm-20230622-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5350145818)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-3.10.4.md)
- [plot](bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-3.11.0.md)
- [plot](bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-base.md)
- [plot](bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f-vs-base.png)

