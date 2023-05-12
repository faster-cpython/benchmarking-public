# Results

- fork: brandtbucher
- version: 3.12.0a7+
- commit hash: [26d9521](https://github.com/brandtbucher/cpython/commit/26d9521)
- commit date: 2023-05-11T15:56:14-07:00
- commit merge base: [0449ffe3a4ddf03367a5ee3d943c89f442b7b407](https://github.com/brandtbucher/cpython/commit/0449ffe3a4ddf03367a5ee3d943c89f442b7b407)
- ref: eval_frame

## linux x86_64 (azure)

- [pystats raw](bm-20230511-azure-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-pystats.json)
- [pystats table](bm-20230511-azure-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4953303725)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521.json)

### vs. 3.10.4

- 1.28x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-3.10.4.md)
- [plot](bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster
- missing benchmarks: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-3.11.0.md)
- [plot](bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-base.md)
- [plot](bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7%2B-26d9521-vs-base.png)

