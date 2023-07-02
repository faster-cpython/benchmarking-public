# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [5b85a49](https://github.com/gvanrossum/cpython/commit/5b85a49)
- commit date: 2023-07-01T14:50:20-07:00
- commit merge base: [822db860eada721742f878653d7ac9364ed8df59](https://github.com/gvanrossum/cpython/commit/822db860eada721742f878653d7ac9364ed8df59)
- ref: tweak_uops

## linux x86_64 (azure)

- [pystats raw](bm-20230701-azure-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-pystats.json)
- [pystats table](bm-20230701-azure-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5433783889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-vs-3.10.4.md)
- [plot](bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-vs-3.11.0.md)
- [plot](bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-vs-3.11.0.png)

### vs. base

- 1.02x slower
- [table](bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-vs-base.md)
- [plot](bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49-vs-base.png)

