# Results

- fork: brandtbucher
- version: 3.12.0a7+
- commit hash: [2f67464](https://github.com/brandtbucher/cpython/commit/2f67464)
- commit date: 2023-05-03T04:17:52-07:00
- commit merge base: [f5c38382f9c40f0017cef086896a8160e313ac9e](https://github.com/brandtbucher/cpython/commit/f5c38382f9c40f0017cef086896a8160e313ac9e)
- ref: load_const_immortal

## linux x86_64 (azure)

- [pystats raw](bm-20230503-azure-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-pystats.json)
- [pystats table](bm-20230503-azure-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4885872441)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464.json)

### vs. 3.10.4

- 1.24x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-vs-3.10.4.md)
- [plot](bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-vs-3.11.0.md)
- [plot](bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-vs-base.md)
- [plot](bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-2f67464-vs-base.png)

