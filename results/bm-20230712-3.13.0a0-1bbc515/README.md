# Results

- fork: faster-cpython
- version: 3.13.0a0
- commit hash: [1bbc515](https://github.com/faster%2dcpython/cpython/commit/1bbc515)
- commit date: 2023-07-12T11:19:59+01:00
- commit merge base: [be1b968dc1e63c3c68e161ddc5a05eb064833440](https://github.com/faster%2dcpython/cpython/commit/be1b968dc1e63c3c68e161ddc5a05eb064833440)
- ref: split_load_global

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5530457639)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20230712-pythonperf1-amd64-faster%252dcpython-split_load_global-3.13.0a0-1bbc515.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230712-pythonperf1-amd64-faster%252dcpython-split_load_global-3.13.0a0-1bbc515-vs-3.10.4.md)
- [plot](bm-20230712-pythonperf1-amd64-faster%252dcpython-split_load_global-3.13.0a0-1bbc515-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x faster (HPT: reliability of 91.26%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230712-pythonperf1-amd64-faster%252dcpython-split_load_global-3.13.0a0-1bbc515-vs-3.11.0.md)
- [plot](bm-20230712-pythonperf1-amd64-faster%252dcpython-split_load_global-3.13.0a0-1bbc515-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 61.37%, 1.00x faster at 99th %ile)
- [table](bm-20230712-pythonperf1-amd64-faster%252dcpython-split_load_global-3.13.0a0-1bbc515-vs-base.md)
- [plot](bm-20230712-pythonperf1-amd64-faster%252dcpython-split_load_global-3.13.0a0-1bbc515-vs-base.png)

