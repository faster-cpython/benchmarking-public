# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [a0bd53a](https://github.com/brandtbucher/cpython/commit/a0bd53a)
- commit date: 2023-06-20T18:52:36-07:00
- commit merge base: [4d140e5e067d3315e163c0f1ac2f80c05ec790c6](https://github.com/brandtbucher/cpython/commit/4d140e5e067d3315e163c0f1ac2f80c05ec790c6)
- ref: to_bool

## linux x86_64 (azure)

- [pystats raw](bm-20230620-azure-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-pystats.json)
- [pystats table](bm-20230620-azure-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5330486982)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a.json)

### vs. 3.10.4

- 1.29x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-3.10.4.md)
- [plot](bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-3.11.0.md)
- [plot](bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-base.md)
- [plot](bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a-vs-base.png)

