# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [28adc90](https://github.com/brandtbucher/cpython/commit/28adc90)
- commit date: 2023-06-10T17:36:52-07:00
- commit merge base: [33c92c4f15539806c8aff8574ff30a8b307e3e4d](https://github.com/brandtbucher/cpython/commit/33c92c4f15539806c8aff8574ff30a8b307e3e4d)
- ref: clean_up_calls

## linux x86_64 (azure)

- [pystats raw](bm-20230610-azure-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-pystats.json)
- [pystats table](bm-20230610-azure-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5232828670)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-vs-3.10.4.md)
- [plot](bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-vs-3.11.0.md)
- [plot](bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-vs-base.md)
- [plot](bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90-vs-base.png)

