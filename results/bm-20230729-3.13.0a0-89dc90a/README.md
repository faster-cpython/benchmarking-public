# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [89dc90a](https://github.com/faster%2dcpython/cpython/commit/89dc90a)
- commit date: 2023-07-29T17:23:35+01:00
- commit merge base: [a1c737b73d3658be0e1d072a340d42e3d96373c6](https://github.com/faster%2dcpython/cpython/commit/a1c737b73d3658be0e1d072a340d42e3d96373c6)
- ref: gc_stats

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5715748716)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230729-linux-x86_64-faster%252dcpython-gc_stats-3.13.0a0-89dc90a.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230729-linux-x86_64-faster%252dcpython-gc_stats-3.13.0a0-89dc90a-vs-3.10.4.md)
- [plot](bm-20230729-linux-x86_64-faster%252dcpython-gc_stats-3.13.0a0-89dc90a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 76.10%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230729-linux-x86_64-faster%252dcpython-gc_stats-3.13.0a0-89dc90a-vs-3.11.0.md)
- [plot](bm-20230729-linux-x86_64-faster%252dcpython-gc_stats-3.13.0a0-89dc90a-vs-3.11.0.png)

