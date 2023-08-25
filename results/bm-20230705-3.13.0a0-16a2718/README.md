# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [16a2718](https://github.com/faster%2dcpython/cpython/commit/16a2718)
- commit date: 2023-07-05T17:16:30+01:00
- commit merge base: [e1d45b8ed43e1590862319fec33539f8adbc0849](https://github.com/faster%2dcpython/cpython/commit/e1d45b8ed43e1590862319fec33539f8adbc0849)
- ref: specialize_more_load

## linux x86_64 (azure)

- [pystats raw](bm-20230705-azure-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-pystats.json)
- [pystats table](bm-20230705-azure-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-pystats.md)

### vs. base

- [pystats diff](bm-20230705-azure-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5485259119)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230705-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-vs-3.10.4.md)
- [plot](bm-20230705-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 89.19%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-vs-3.11.0.md)
- [plot](bm-20230705-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 92.11%, 1.00x faster at 99th %ile)
- [table](bm-20230705-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-vs-base.md)
- [plot](bm-20230705-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-16a2718-vs-base.png)

