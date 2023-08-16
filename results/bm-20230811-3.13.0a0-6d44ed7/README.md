# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [6d44ed7](https://github.com/faster%2dcpython/cpython/commit/6d44ed7)
- commit date: 2023-08-11T13:23:01+01:00
- commit merge base: [42429d3b9adb8af1eadcfa155f6e8422a254ec67](https://github.com/faster%2dcpython/cpython/commit/42429d3b9adb8af1eadcfa155f6e8422a254ec67)
- ref: remove_cframe

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5881035764)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230811-linux-x86_64-faster%252dcpython-remove_cframe-3.13.0a0-6d44ed7.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230811-linux-x86_64-faster%252dcpython-remove_cframe-3.13.0a0-6d44ed7-vs-3.10.4.md)
- [plot](bm-20230811-linux-x86_64-faster%252dcpython-remove_cframe-3.13.0a0-6d44ed7-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230811-linux-x86_64-faster%252dcpython-remove_cframe-3.13.0a0-6d44ed7-vs-3.11.0.md)
- [plot](bm-20230811-linux-x86_64-faster%252dcpython-remove_cframe-3.13.0a0-6d44ed7-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230811-linux-x86_64-faster%252dcpython-remove_cframe-3.13.0a0-6d44ed7-vs-base.md)
- [plot](bm-20230811-linux-x86_64-faster%252dcpython-remove_cframe-3.13.0a0-6d44ed7-vs-base.png)

