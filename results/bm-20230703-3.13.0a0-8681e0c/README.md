# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [8681e0c](https://github.com/gvanrossum/cpython/commit/8681e0c)
- commit date: 2023-07-03T18:28:09-07:00
- commit merge base: [3406f8cce542ea4edf4153c0fac5216df283a9b1](https://github.com/gvanrossum/cpython/commit/3406f8cce542ea4edf4153c0fac5216df283a9b1)
- ref: jump_uops

## linux x86_64 (azure)

- [pystats raw](bm-20230703-azure-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-pystats.json)
- [pystats table](bm-20230703-azure-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5450177608)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-vs-3.10.4.md)
- [plot](bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-vs-3.11.0.md)
- [plot](bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-vs-base.md)
- [plot](bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c-vs-base.png)

