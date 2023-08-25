# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [b32b56c](https://github.com/faster%2dcpython/cpython/commit/b32b56c)
- commit date: 2023-08-10T07:00:11+01:00
- commit merge base: [37d8b904f8b5b660f556597b21c0933b841d18de](https://github.com/faster%2dcpython/cpython/commit/37d8b904f8b5b660f556597b21c0933b841d18de)
- ref: gc_threshold_2000

## linux x86_64 (azure)

- [pystats raw](bm-20230810-azure-x86_64-faster%252dcpython-gc_threshold_2000-3.13.0a0-b32b56c-pystats.json)
- [pystats table](bm-20230810-azure-x86_64-faster%252dcpython-gc_threshold_2000-3.13.0a0-b32b56c-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5833779742)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230810-linux-x86_64-faster%252dcpython-gc_threshold_2000-3.13.0a0-b32b56c.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230810-linux-x86_64-faster%252dcpython-gc_threshold_2000-3.13.0a0-b32b56c-vs-3.10.4.md)
- [plot](bm-20230810-linux-x86_64-faster%252dcpython-gc_threshold_2000-3.13.0a0-b32b56c-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.06x faster (HPT: reliability of 90.66%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230810-linux-x86_64-faster%252dcpython-gc_threshold_2000-3.13.0a0-b32b56c-vs-3.11.0.md)
- [plot](bm-20230810-linux-x86_64-faster%252dcpython-gc_threshold_2000-3.13.0a0-b32b56c-vs-3.11.0.png)

