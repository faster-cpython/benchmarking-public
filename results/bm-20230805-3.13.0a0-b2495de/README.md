# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [b2495de](https://github.com/brandtbucher/cpython/commit/b2495de)
- commit date: 2023-08-05T00:38:26-07:00
- commit merge base: [16c9415fba4972743f1944ebc44946e475e68bc4](https://github.com/brandtbucher/cpython/commit/16c9415fba4972743f1944ebc44946e475e68bc4)
- ref: un_materialize_alt

## linux x86_64 (azure)

- [pystats raw](bm-20230805-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-pystats.json)
- [pystats table](bm-20230805-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-pystats.md)

### vs. base

- [pystats diff](bm-20230805-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5789121078)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-3.10.4.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-3.11.0.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-base.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de-vs-base.png)

