# Results

- fork: brandtbucher
- version: 3.13.0a0
- commit hash: [e4c97dd](https://github.com/brandtbucher/cpython/commit/e4c97dd)
- commit date: 2023-07-05T15:54:08-07:00
- commit merge base: [ede89af605b1c0442353435ad22195c16274f65d](https://github.com/brandtbucher/cpython/commit/ede89af605b1c0442353435ad22195c16274f65d)
- ref: justin_symbols

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/5470028127)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd-vs-3.10.4.md)
- [plot](bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x faster (HPT: reliability of 99.20%, 1.00x slower at 99th %ile)
- missing benchmarks: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
- [table](bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd-vs-3.11.0.md)
- [plot](bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 81.69%, 1.00x slower at 99th %ile)
- [table](bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd-vs-base.md)
- [plot](bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd-vs-base.png)

