# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [17ae178](https://github.com/faster%2dcpython/cpython/commit/17ae178)
- commit date: 2023-08-10T00:43:52+01:00
- commit merge base: [37d8b904f8b5b660f556597b21c0933b841d18de](https://github.com/faster%2dcpython/cpython/commit/37d8b904f8b5b660f556597b21c0933b841d18de)
- ref: always_allocate_valu

## linux x86_64 (azure)

- [pystats raw](bm-20230810-azure-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-pystats.json)
- [pystats table](bm-20230810-azure-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5822096943)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230810-linux-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230810-linux-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-vs-3.10.4.md)
- [plot](bm-20230810-linux-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230810-linux-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-vs-3.11.0.md)
- [plot](bm-20230810-linux-x86_64-faster%252dcpython-always_allocate_valu-3.13.0a0-17ae178-vs-3.11.0.png)

