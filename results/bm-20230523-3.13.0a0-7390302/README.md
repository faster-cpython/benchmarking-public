# Results

- fork: kumaraditya303
- version: 3.13.0a0
- commit hash: [7390302](https://github.com/kumaraditya303/cpython/commit/7390302)
- commit date: 2023-05-23T05:08:32+00:00
- commit merge base: [5ecd8c85f934e13a5ff98db6539d89e0c7c03f2d](https://github.com/kumaraditya303/cpython/commit/5ecd8c85f934e13a5ff98db6539d89e0c7c03f2d)
- ref: no_register

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5057411573)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: aiohttp, chameleon, dask, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-3.10.4.md)
- [plot](bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: aiohttp, chameleon, dask, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-3.11.0.md)
- [plot](bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-3.11.0.png)

### vs. base

- 1.01x faster
- missing benchmarks: 🔴 dask
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib
- [table](bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-base.md)
- [plot](bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302-vs-base.png)

