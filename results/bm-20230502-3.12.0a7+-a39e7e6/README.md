# Results

- fork: brandtbucher
- version: 3.12.0a7+
- commit hash: [a39e7e6](https://github.com/brandtbucher/cpython/commit/a39e7e6)
- commit date: 2023-05-02T21:39:37-07:00
- commit merge base: [da1980afcb8820ffaa0574df735bc39b1a276a76](https://github.com/brandtbucher/cpython/commit/da1980afcb8820ffaa0574df735bc39b1a276a76)
- ref: load_const_immortal

## linux x86_64 (azure)

- [pystats raw](bm-20230502-azure-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-pystats.json)
- [pystats table](bm-20230502-azure-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4879039553)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6.json)

### vs. 3.10.4

- 1.24x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-vs-3.10.4.md)
- [plot](bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-vs-3.11.0.md)
- [plot](bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-vs-base.md)
- [plot](bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7%2B-a39e7e6-vs-base.png)

