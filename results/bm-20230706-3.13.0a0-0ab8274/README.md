# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [0ab8274](https://github.com/brandtbucher/cpython/commit/0ab8274)
- commit date: 2023-07-06T16:01:44-07:00
- commit merge base: [67a798888dcde13bbb1e17cfcc3c742c94e67a07](https://github.com/brandtbucher/cpython/commit/67a798888dcde13bbb1e17cfcc3c742c94e67a07)
- ref: un_materialize

## linux x86_64 (azure)

- [pystats raw](bm-20230706-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-pystats.json)
- [pystats table](bm-20230706-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-pystats.md)

### vs. base

- [pystats diff](bm-20230706-azure-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5480980605)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.10.4.md)
- [plot](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.11.0.md)
- [plot](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-base.md)
- [plot](bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274-vs-base.png)

