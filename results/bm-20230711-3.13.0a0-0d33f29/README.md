# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [0d33f29](https://github.com/gvanrossum/cpython/commit/0d33f29)
- commit date: 2023-07-11T10:55:45-07:00
- commit merge base: [d0b7e18262e69dd4b8252e804e4f98fc9533bcd6](https://github.com/gvanrossum/cpython/commit/d0b7e18262e69dd4b8252e804e4f98fc9533bcd6)
- ref: new_for_iter_uops

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5524214422)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29-vs-3.10.4.md)
- [plot](bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 51.20%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29-vs-3.11.0.md)
- [plot](bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- [table](bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29-vs-base.md)
- [plot](bm-20230711-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-0d33f29-vs-base.png)

