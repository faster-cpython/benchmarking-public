# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [47205b2](https://github.com/brandtbucher/cpython/commit/47205b2)
- commit date: 2023-06-16T03:08:49-07:00
- commit merge base: [2beab5bdef5fa2a00a59371e6137f769586b7404](https://github.com/brandtbucher/cpython/commit/2beab5bdef5fa2a00a59371e6137f769586b7404)
- ref: clean_up_calls

## linux x86_64 (azure)

- [pystats raw](bm-20230616-azure-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-pystats.json)
- [pystats table](bm-20230616-azure-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5294106024)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-vs-3.10.4.md)
- [plot](bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-vs-3.11.0.md)
- [plot](bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-vs-base.md)
- [plot](bm-20230616-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-47205b2-vs-base.png)

