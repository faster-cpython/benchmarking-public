# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [8abbc6a](https://github.com/brandtbucher/cpython/commit/8abbc6a)
- commit date: 2023-08-03T13:38:25-07:00
- commit merge base: [14fbd4e6b16dcbcbff448b047f7e2faa27bbedba](https://github.com/brandtbucher/cpython/commit/14fbd4e6b16dcbcbff448b047f7e2faa27bbedba)
- ref: immortal_increfs

## linux x86_64 (azure)

- [pystats raw](bm-20230803-azure-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-pystats.json)
- [pystats table](bm-20230803-azure-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-pystats.md)

### vs. base

- [pystats diff](bm-20230803-azure-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5755675674)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-3.10.4.md)
- [plot](bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 84.60%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-3.11.0.md)
- [plot](bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 52.30%, 1.00x slower at 99th %ile)
- [table](bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-base.md)
- [plot](bm-20230803-linux-x86_64-brandtbucher-immortal_increfs-3.13.0a0-8abbc6a-vs-base.png)

