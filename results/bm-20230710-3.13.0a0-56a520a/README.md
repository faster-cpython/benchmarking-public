# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [56a520a](https://github.com/brandtbucher/cpython/commit/56a520a)
- commit date: 2023-07-10T16:02:42-07:00
- commit merge base: [a840806d338805fe74a9de01081d30da7605a29f](https://github.com/brandtbucher/cpython/commit/a840806d338805fe74a9de01081d30da7605a29f)
- ref: untrack_dicts

## linux x86_64 (azure)

- [pystats raw](bm-20230710-azure-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-pystats.json)
- [pystats table](bm-20230710-azure-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-pystats.md)

### vs. base

- [pystats diff](bm-20230710-azure-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5513844240)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-vs-3.10.4.md)
- [plot](bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 79.14%, 1.00x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-vs-3.11.0.md)
- [plot](bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 72.07%, 1.00x faster at 99th %ile)
- [table](bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-vs-base.md)
- [plot](bm-20230710-linux-x86_64-brandtbucher-untrack_dicts-3.13.0a0-56a520a-vs-base.png)

