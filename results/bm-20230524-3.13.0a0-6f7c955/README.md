# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [6f7c955](https://github.com/gvanrossum/cpython/commit/6f7c955)
- commit date: 2023-05-24T20:33:58-07:00
- commit merge base: [b1cb30ec8639e4e65f62e8f6cd44e979640431c8](https://github.com/gvanrossum/cpython/commit/b1cb30ec8639e4e65f62e8f6cd44e979640431c8)
- ref: split_ops

## linux x86_64 (azure)

- [pystats raw](bm-20230524-azure-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-pystats.json)
- [pystats table](bm-20230524-azure-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5083302652)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955.json)

### vs. 3.10.4

- 1.28x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-vs-3.10.4.md)
- [plot](bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-vs-3.11.0.md)
- [plot](bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-vs-base.md)
- [plot](bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955-vs-base.png)

