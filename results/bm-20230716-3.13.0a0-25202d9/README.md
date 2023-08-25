# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [25202d9](https://github.com/brandtbucher/cpython/commit/25202d9)
- commit date: 2023-07-16T07:55:41-07:00
- commit merge base: [8c177294899b621fe04ae755abd41b4d319dd4b5](https://github.com/brandtbucher/cpython/commit/8c177294899b621fe04ae755abd41b4d319dd4b5)
- ref: un_materialize_alt

## linux x86_64 (azure)

- [pystats raw](bm-20230716-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-pystats.json)
- [pystats table](bm-20230716-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-pystats.md)

### vs. base

- [pystats diff](bm-20230716-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5569480032)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-vs-3.10.4.md)
- [plot](bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 73.75%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-vs-3.11.0.md)
- [plot](bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- [table](bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-vs-base.md)
- [plot](bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9-vs-base.png)

