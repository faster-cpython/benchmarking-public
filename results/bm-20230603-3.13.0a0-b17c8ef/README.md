# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [b17c8ef](https://github.com/faster%2dcpython/cpython/commit/b17c8ef)
- commit date: 2023-06-03T03:12:12+01:00
- commit merge base: [06893403668961fdbd5d9ece18162eb3470fc8dd](https://github.com/faster%2dcpython/cpython/commit/06893403668961fdbd5d9ece18162eb3470fc8dd)
- ref: safe_decref

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5178440638)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230603-linux-x86_64-faster%252dcpython-safe_decref-3.13.0a0-b17c8ef.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230603-linux-x86_64-faster%252dcpython-safe_decref-3.13.0a0-b17c8ef-vs-3.10.4.md)
- [plot](bm-20230603-linux-x86_64-faster%252dcpython-safe_decref-3.13.0a0-b17c8ef-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 93.84%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230603-linux-x86_64-faster%252dcpython-safe_decref-3.13.0a0-b17c8ef-vs-3.11.0.md)
- [plot](bm-20230603-linux-x86_64-faster%252dcpython-safe_decref-3.13.0a0-b17c8ef-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- [table](bm-20230603-linux-x86_64-faster%252dcpython-safe_decref-3.13.0a0-b17c8ef-vs-base.md)
- [plot](bm-20230603-linux-x86_64-faster%252dcpython-safe_decref-3.13.0a0-b17c8ef-vs-base.png)

