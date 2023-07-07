# Results

- fork: mdboom
- version: 3.13.0a0
- commit hash: [0b85a0d](https://github.com/mdboom/cpython/commit/0b85a0d)
- commit date: 2023-07-05T10:54:18-04:00
- commit merge base: [12a98138083589314d3da14bc97f2d8517947437](https://github.com/mdboom/cpython/commit/12a98138083589314d3da14bc97f2d8517947437)
- ref: pystats_test

## linux x86_64 (azure)

- [pystats raw](bm-20230705-azure-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-pystats.json)
- [pystats table](bm-20230705-azure-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-pystats.md)

### vs. base

- [pystats diff](bm-20230705-azure-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5466296358)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-vs-3.10.4.md)
- [plot](bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-vs-3.11.0.md)
- [plot](bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-vs-base.md)
- [plot](bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d-vs-base.png)

