# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [e03a937](https://github.com/brandtbucher/cpython/commit/e03a937)
- commit date: 2023-08-04T16:08:14-07:00
- commit merge base: [2c25bd82f46df72c89ca5bca10eaa06137ab8290](https://github.com/brandtbucher/cpython/commit/2c25bd82f46df72c89ca5bca10eaa06137ab8290)
- ref: binary_subscr_str_in

## linux x86_64 (azure)

- [pystats raw](bm-20230804-azure-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-pystats.json)
- [pystats table](bm-20230804-azure-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-pystats.md)

### vs. base

- [pystats diff](bm-20230804-azure-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5767335165)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-3.10.4.md)
- [plot](bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 74.05%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-3.11.0.md)
- [plot](bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- [table](bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-base.md)
- [plot](bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937-vs-base.png)

