# Results

- fork: adr26
- version: 3.12.0a7+
- commit hash: [4f0355f](https://github.com/adr26/cpython/commit/4f0355f)
- commit date: 2023-05-16T21:07:43+01:00
- commit merge base: [20e994c535fea33b827e69323f80fec056a76250](https://github.com/adr26/cpython/commit/20e994c535fea33b827e69323f80fec056a76250)
- ref: condvar

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5009139216)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f.json)

### vs. 3.10.4

- 1.17x faster
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-3.10.4.md)
- [plot](bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-3.10.4.png)

### vs. 3.11.0

- 1.05x faster
- missing benchmarks: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-3.11.0.md)
- [plot](bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-base.md)
- [plot](bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7%2B-4f0355f-vs-base.png)

