# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [1df353e](https://github.com/faster%2dcpython/cpython/commit/1df353e)
- commit date: 2023-06-18T16:15:13+01:00
- commit merge base: [155577de1b6a7f4404b2bf90bcc1a588201550da](https://github.com/faster%2dcpython/cpython/commit/155577de1b6a7f4404b2bf90bcc1a588201550da)
- ref: specialize_calls_to_

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5333116681)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-3.10.4.md)
- [plot](bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-3.10.4.png)

### vs. 3.11.0

- 1.06x faster
- missing benchmarks: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-3.11.0.md)
- [plot](bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-base.md)
- [plot](bm-20230618-pythonperf2-x86_64-faster%252dcpython-specialize_calls_to_-3.13.0a0-1df353e-vs-base.png)

