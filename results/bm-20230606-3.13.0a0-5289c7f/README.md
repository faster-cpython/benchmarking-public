# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [5289c7f](https://github.com/brandtbucher/cpython/commit/5289c7f)
- commit date: 2023-06-06T16:47:13-07:00
- commit merge base: [eaff9c39aa1a70d401521847cc35bec883ae9772](https://github.com/brandtbucher/cpython/commit/eaff9c39aa1a70d401521847cc35bec883ae9772)
- ref: specialize_unary_not

## linux x86_64 (azure)

- [pystats raw](bm-20230606-azure-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-pystats.json)
- [pystats table](bm-20230606-azure-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5194423276)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-3.10.4.md)
- [plot](bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-3.11.0.md)
- [plot](bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-3.11.0.png)

### vs. base

- 1.02x slower
- [table](bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-base.md)
- [plot](bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f-vs-base.png)

