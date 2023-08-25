# Results

- fork: faster-cpython
- version: 3.12.0a7+
- commit hash: [f190abf](https://github.com/faster%2dcpython/cpython/commit/f190abf)
- commit date: 2023-05-12T22:03:34+01:00
- commit merge base: [f7df17394906f2af51afef3c8ccaaab3847b059c](https://github.com/faster%2dcpython/cpython/commit/f7df17394906f2af51afef3c8ccaaab3847b059c)
- ref: no_predict

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5013538040)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230512-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a7%2B-f190abf.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230512-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a7%2B-f190abf-vs-3.10.4.md)
- [plot](bm-20230512-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a7%2B-f190abf-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230512-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a7%2B-f190abf-vs-3.11.0.md)
- [plot](bm-20230512-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a7%2B-f190abf-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- [table](bm-20230512-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a7%2B-f190abf-vs-base.md)
- [plot](bm-20230512-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a7%2B-f190abf-vs-base.png)

