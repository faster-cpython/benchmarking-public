# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [0463633](https://github.com/brandtbucher/cpython/commit/0463633)
- commit date: 2023-06-09T14:15:22-07:00
- commit merge base: [eaff9c39aa1a70d401521847cc35bec883ae9772](https://github.com/brandtbucher/cpython/commit/eaff9c39aa1a70d401521847cc35bec883ae9772)
- ref: to_bool

## linux x86_64 (azure)

- [pystats raw](bm-20230609-azure-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-pystats.json)
- [pystats table](bm-20230609-azure-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5226326278)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-3.10.4.md)
- [plot](bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x faster (HPT: reliability of 99.82%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-3.11.0.md)
- [plot](bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- [table](bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-base.md)
- [plot](bm-20230609-linux-x86_64-brandtbucher-to_bool-3.13.0a0-0463633-vs-base.png)

