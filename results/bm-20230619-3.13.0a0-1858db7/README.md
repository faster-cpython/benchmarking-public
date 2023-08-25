# Results

- fork: python
- version: 3.13.0a0
- commit hash: [1858db7](https://github.com/python/cpython/commit/1858db7)
- commit date: 2023-06-19T17:09:04+00:00
- ref: 1858db7cbdbf41aa600c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5315068096)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7-vs-3.10.4.md)
- [plot](bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 72.38%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7-vs-3.11.0.md)
- [plot](bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7-vs-3.11.0.png)

