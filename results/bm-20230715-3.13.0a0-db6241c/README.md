# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [db6241c](https://github.com/gvanrossum/cpython/commit/db6241c)
- commit date: 2023-07-15T13:46:39-07:00
- commit merge base: [d46a42fd8e8915e03cc211ab9163058b6365ab0f](https://github.com/gvanrossum/cpython/commit/d46a42fd8e8915e03cc211ab9163058b6365ab0f)
- ref: simple_calls_with_xu

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5564131756)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c.json)

### vs. 3.10.4

- 1.24x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c-vs-3.10.4.md)
- [plot](bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c-vs-3.10.4.png)

### vs. 3.11.0

- 1.00x slower
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c-vs-3.11.0.md)
- [plot](bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c-vs-3.11.0.png)

### vs. base

- 1.04x slower
- [table](bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c-vs-base.md)
- [plot](bm-20230715-linux-x86_64-gvanrossum-simple_calls_with_xu-3.13.0a0-db6241c-vs-base.png)

