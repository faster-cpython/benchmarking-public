# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [930262f](https://github.com/brandtbucher/cpython/commit/930262f)
- commit date: 2023-08-05T15:55:44-07:00
- commit merge base: [2c25bd82f46df72c89ca5bca10eaa06137ab8290](https://github.com/brandtbucher/cpython/commit/2c25bd82f46df72c89ca5bca10eaa06137ab8290)
- ref: tracing

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5777627754)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-3.10.4.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.94%, 1.01x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-3.11.0.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- [table](bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-base.md)
- [plot](bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f-vs-base.png)

