# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [d00eefe](https://github.com/brandtbucher/cpython/commit/d00eefe)
- commit date: 2023-07-07T16:35:31-07:00
- commit merge base: [80b9b3a51757ebb1e3547afc349a229706eadfde](https://github.com/brandtbucher/cpython/commit/80b9b3a51757ebb1e3547afc349a229706eadfde)
- ref: un_materialize_alt

## linux x86_64 (azure)

- [pystats raw](bm-20230707-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-pystats.json)
- [pystats table](bm-20230707-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-pystats.md)

### vs. base

- [pystats diff](bm-20230707-azure-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5491445080)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-vs-3.10.4.md)
- [plot](bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-vs-3.11.0.md)
- [plot](bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-vs-base.md)
- [plot](bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe-vs-base.png)

