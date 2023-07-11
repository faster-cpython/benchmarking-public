# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [66a6bc3](https://github.com/faster%2dcpython/cpython/commit/66a6bc3)
- commit date: 2023-07-10T16:32:42-07:00
- commit merge base: [22988c323ad621b9f47b6cb640b80ac806e26368](https://github.com/faster%2dcpython/cpython/commit/22988c323ad621b9f47b6cb640b80ac806e26368)
- ref: micro_op_jump_if_non

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5517779334)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20230710-pythonperf2-x86_64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf2-x86_64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.10.4.md)
- [plot](bm-20230710-pythonperf2-x86_64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf2-x86_64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.11.0.md)
- [plot](bm-20230710-pythonperf2-x86_64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230710-pythonperf2-x86_64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-base.md)
- [plot](bm-20230710-pythonperf2-x86_64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5517797991)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230710-pythonperf1-amd64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3.json)

### vs. 3.10.4

- 1.13x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf1-amd64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.10.4.md)
- [plot](bm-20230710-pythonperf1-amd64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-pythonperf1-amd64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.11.0.md)
- [plot](bm-20230710-pythonperf1-amd64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230710-pythonperf1-amd64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-base.md)
- [plot](bm-20230710-pythonperf1-amd64-faster%252dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3-vs-base.png)

