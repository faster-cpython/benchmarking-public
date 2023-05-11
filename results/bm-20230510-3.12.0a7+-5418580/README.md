# Results

- fork: faster-cpython
- version: 3.12.0a7+
- commit hash: [5418580](https://github.com/faster%2dcpython/cpython/commit/5418580)
- commit date: 2023-05-10T20:55:08+01:00
- commit merge base: [e629ab6adf19544d5ee3f87bd1a9e9ff90808a08](https://github.com/faster%2dcpython/cpython/commit/e629ab6adf19544d5ee3f87bd1a9e9ff90808a08)
- ref: instrument_all_possi

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4947515993)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580.json)

### vs. 3.10.4

- 1.27x faster \*
- missing benchmarks: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-3.10.4.md)
- [plot](bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-3.11.0.md)
- [plot](bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-base.md)
- [plot](bm-20230510-pythonperf2-x86_64-faster%252dcpython-instrument_all_possi-3.12.0a7%2B-5418580-vs-base.png)

