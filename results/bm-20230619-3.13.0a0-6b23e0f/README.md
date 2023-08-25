# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [6b23e0f](https://github.com/gvanrossum/cpython/commit/6b23e0f)
- commit date: 2023-06-19T13:18:27-07:00
- commit merge base: [1858db7cbdbf41aa600c954c15224307bf81a258](https://github.com/gvanrossum/cpython/commit/1858db7cbdbf41aa600c954c15224307bf81a258)
- ref: optim_exec

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5317170357)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-3.10.4.md)
- [plot](bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 87.56%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-3.11.0.md)
- [plot](bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 55.79%, 1.00x slower at 99th %ile)
- [table](bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-base.md)
- [plot](bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f-vs-base.png)

