# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [3259d6e](https://github.com/gvanrossum/cpython/commit/3259d6e)
- commit date: 2023-05-30T14:32:11-07:00
- commit merge base: [68c75c31536e8c87901934f2d6da81f54f4334f9](https://github.com/gvanrossum/cpython/commit/68c75c31536e8c87901934f2d6da81f54f4334f9)
- ref: split_ops

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5131667204)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e.json)

### vs. 3.10.4

- 1.27x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e-vs-3.10.4.md)
- [plot](bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e-vs-3.11.0.md)
- [plot](bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e-vs-base.md)
- [plot](bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e-vs-base.png)

