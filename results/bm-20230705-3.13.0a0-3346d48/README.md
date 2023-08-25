# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [3346d48](https://github.com/brandtbucher/cpython/commit/3346d48)
- commit date: 2023-07-05T15:30:50-07:00
- commit merge base: [ede89af605b1c0442353435ad22195c16274f65d](https://github.com/brandtbucher/cpython/commit/ede89af605b1c0442353435ad22195c16274f65d)
- ref: justin

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5469837981)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48-vs-3.10.4.md)
- [plot](bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x faster (HPT: reliability of 97.98%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48-vs-3.11.0.md)
- [plot](bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.92%, 1.00x slower at 99th %ile)
- [table](bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48-vs-base.md)
- [plot](bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48-vs-base.png)

