# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [c5f2067](https://github.com/brandtbucher/cpython/commit/c5f2067)
- commit date: 2023-06-29T12:53:31-07:00
- commit merge base: [3c70d467c148875f2ce17bacab8909ecc3e9fc1d](https://github.com/brandtbucher/cpython/commit/3c70d467c148875f2ce17bacab8909ecc3e9fc1d)
- ref: un_materialize

## linux x86_64 (azure)

- [pystats raw](bm-20230629-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-pystats.json)
- [pystats table](bm-20230629-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5416161307)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-vs-3.10.4.md)
- [plot](bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-vs-3.11.0.md)
- [plot](bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-vs-base.md)
- [plot](bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067-vs-base.png)

