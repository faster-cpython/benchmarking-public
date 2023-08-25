# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [83ffca9](https://github.com/faster%2dcpython/cpython/commit/83ffca9)
- commit date: 2023-08-05T03:01:07+01:00
- commit merge base: [2ac103c346ffe9d0e4c146402ce215c5ce6c1ef2](https://github.com/faster%2dcpython/cpython/commit/2ac103c346ffe9d0e4c146402ce215c5ce6c1ef2)
- ref: tweak_ints_monitorin

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5796074095)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-3.10.4.md)
- [plot](bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 83.24%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-3.11.0.md)
- [plot](bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 81.08%, 1.00x slower at 99th %ile)
- [table](bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-base.md)
- [plot](bm-20230805-pythonperf2-x86_64-faster%252dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9-vs-base.png)

