# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [4ccb873](https://github.com/gvanrossum/cpython/commit/4ccb873)
- commit date: 2023-07-12T09:48:20-07:00
- commit merge base: [7f55f58b6c97306da350f5b441d26f859e9d8f16](https://github.com/gvanrossum/cpython/commit/7f55f58b6c97306da350f5b441d26f859e9d8f16)
- ref: new_for_iter_uops

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5534304413)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873-vs-3.10.4.md)
- [plot](bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873-vs-3.11.0.md)
- [plot](bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873-vs-base.md)
- [plot](bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873-vs-base.png)

