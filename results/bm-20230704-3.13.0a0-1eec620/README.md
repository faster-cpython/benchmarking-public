# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [1eec620](https://github.com/faster%2dcpython/cpython/commit/1eec620)
- commit date: 2023-07-04T04:50:21+01:00
- commit merge base: [80f1c6c49b4cd2bf698eb2bc3d2f3da904880dd2](https://github.com/faster%2dcpython/cpython/commit/80f1c6c49b4cd2bf698eb2bc3d2f3da904880dd2)
- ref: specialize_more_load

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5462574068)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230704-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-1eec620.json)

### vs. 3.10.4

- 1.27x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230704-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-1eec620-vs-3.10.4.md)
- [plot](bm-20230704-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-1eec620-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230704-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-1eec620-vs-3.11.0.md)
- [plot](bm-20230704-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-1eec620-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230704-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-1eec620-vs-base.md)
- [plot](bm-20230704-pythonperf2-x86_64-faster%252dcpython-specialize_more_load-3.13.0a0-1eec620-vs-base.png)

