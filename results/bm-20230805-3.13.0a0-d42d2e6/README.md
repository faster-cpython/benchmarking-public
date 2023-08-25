# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [d42d2e6](https://github.com/brandtbucher/cpython/commit/d42d2e6)
- commit date: 2023-08-05T12:05:53-07:00
- commit merge base: [16c9415fba4972743f1944ebc44946e475e68bc4](https://github.com/brandtbucher/cpython/commit/16c9415fba4972743f1944ebc44946e475e68bc4)
- ref: un_materialize_alt

## linux x86_64 (azure)

- [pystats raw](bm-20230805-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-pystats.json)
- [pystats table](bm-20230805-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-pystats.md)

### vs. base

- [pystats diff](bm-20230805-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5802731260)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-3.10.4.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 85.14%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-3.11.0.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 67.39%, 1.00x faster at 99th %ile)
- [table](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-base.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6-vs-base.png)

