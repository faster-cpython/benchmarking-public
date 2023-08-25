# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [0ccd3bb](https://github.com/faster%2dcpython/cpython/commit/0ccd3bb)
- commit date: 2023-08-05T01:57:54+01:00
- commit merge base: [2ac103c346ffe9d0e4c146402ce215c5ce6c1ef2](https://github.com/faster%2dcpython/cpython/commit/2ac103c346ffe9d0e4c146402ce215c5ce6c1ef2)
- ref: tweak_ints_monitorin

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5795408279)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-3.10.4.md)
- [plot](bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 64.34%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-3.11.0.md)
- [plot](bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 88.93%, 1.00x slower at 99th %ile)
- [table](bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-base.md)
- [plot](bm-20230805-linux-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb-vs-base.png)

