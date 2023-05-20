# Results

- fork: brandtbucher
- version: 3.12.0a7+
- commit hash: [33cd56d](https://github.com/brandtbucher/cpython/commit/33cd56d)
- commit date: 2023-05-19T14:41:26-07:00
- commit merge base: [3bc94e678f2961eafc9d665898d73afc6204d314](https://github.com/brandtbucher/cpython/commit/3bc94e678f2961eafc9d665898d73afc6204d314)
- ref: load_const_immortal

## linux x86_64 (azure)

- [pystats raw](bm-20230519-azure-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-pystats.json)
- [pystats table](bm-20230519-azure-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5028892067)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d.json)

### vs. 3.10.4

- 1.28x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-vs-3.10.4.md)
- [plot](bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-vs-3.11.0.md)
- [plot](bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-vs-base.md)
- [plot](bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-33cd56d-vs-base.png)

