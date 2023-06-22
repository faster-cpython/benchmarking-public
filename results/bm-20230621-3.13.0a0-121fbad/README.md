# Results

- fork: gvanrossum
- version: 3.13.0a0
- commit hash: [121fbad](https://github.com/gvanrossum/cpython/commit/121fbad)
- commit date: 2023-06-21T17:27:42-07:00
- commit merge base: [7f97c8e367869e2aebe9f28bc5f8d4ce36448878](https://github.com/gvanrossum/cpython/commit/7f97c8e367869e2aebe9f28bc5f8d4ce36448878)
- ref: optim_exec

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5341310101)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-3.10.4.md)
- [plot](bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-3.11.0.md)
- [plot](bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-base.md)
- [plot](bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad-vs-base.png)

