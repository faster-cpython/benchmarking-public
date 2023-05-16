# Results

- fork: faster-cpython
- version: 3.12.0a7+
- commit hash: [4d1b4d4](https://github.com/faster%2dcpython/cpython/commit/4d1b4d4)
- commit date: 2023-05-12T07:42:11+01:00
- commit merge base: [b378d991f8cd41c33416e590cb83472cce1d6b98](https://github.com/faster%2dcpython/cpython/commit/b378d991f8cd41c33416e590cb83472cce1d6b98)
- ref: no_local_eval_breake

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4994349254)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230512-pythonperf2-x86_64-faster%252dcpython-no_local_eval_breake-3.12.0a7%2B-4d1b4d4.json)

### vs. 3.10.4

- 1.31x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230512-pythonperf2-x86_64-faster%252dcpython-no_local_eval_breake-3.12.0a7%2B-4d1b4d4-vs-3.10.4.md)
- [plot](bm-20230512-pythonperf2-x86_64-faster%252dcpython-no_local_eval_breake-3.12.0a7%2B-4d1b4d4-vs-3.10.4.png)

### vs. 3.11.0

- 1.08x faster
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230512-pythonperf2-x86_64-faster%252dcpython-no_local_eval_breake-3.12.0a7%2B-4d1b4d4-vs-3.11.0.md)
- [plot](bm-20230512-pythonperf2-x86_64-faster%252dcpython-no_local_eval_breake-3.12.0a7%2B-4d1b4d4-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230512-pythonperf2-x86_64-faster%252dcpython-no_local_eval_breake-3.12.0a7%2B-4d1b4d4-vs-base.md)
- [plot](bm-20230512-pythonperf2-x86_64-faster%252dcpython-no_local_eval_breake-3.12.0a7%2B-4d1b4d4-vs-base.png)

