# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [328cfd4](https://github.com/faster%2dcpython/cpython/commit/328cfd4)
- commit date: 2023-08-13T06:06:44+01:00
- commit merge base: [2ac103c346ffe9d0e4c146402ce215c5ce6c1ef2](https://github.com/faster%2dcpython/cpython/commit/2ac103c346ffe9d0e4c146402ce215c5ce6c1ef2)
- ref: incremental_gc

## linux x86_64 (azure)

- [pystats raw](bm-20230813-azure-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-pystats.json)
- [pystats table](bm-20230813-azure-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-pystats.md)

### vs. base

- [pystats diff](bm-20230813-azure-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5949748514)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230813-linux-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230813-linux-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-vs-3.10.4.md)
- [plot](bm-20230813-linux-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 82.78%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230813-linux-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-vs-3.11.0.md)
- [plot](bm-20230813-linux-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.02x faster (HPT: reliability of 55.06%, 1.00x slower at 99th %ile)
- [table](bm-20230813-linux-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-vs-base.md)
- [plot](bm-20230813-linux-x86_64-faster%252dcpython-incremental_gc-3.13.0a0-328cfd4-vs-base.png)

