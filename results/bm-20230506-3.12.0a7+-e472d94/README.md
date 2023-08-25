# Results

- fork: ericsnowcurrently
- version: 3.12.0a7+
- commit hash: [e472d94](https://github.com/ericsnowcurrently/cpython/commit/e472d94)
- commit date: 2023-05-06T17:56:19-06:00
- commit merge base: [92d8bfffbf377e91d8b92666525cb8700bb1d5e8](https://github.com/ericsnowcurrently/cpython/commit/92d8bfffbf377e91d8b92666525cb8700bb1d5e8)
- ref: immortalize_empty_ke

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4904482691)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7%2B-e472d94.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster \* (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7%2B-e472d94-vs-3.10.4.md)
- [plot](bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7%2B-e472d94-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x slower \* (HPT: reliability of 99.08%, 1.00x slower at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7%2B-e472d94-vs-3.11.0.md)
- [plot](bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7%2B-e472d94-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.62%, 1.00x slower at 99th %ile)
- [table](bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7%2B-e472d94-vs-base.md)
- [plot](bm-20230506-linux-x86_64-ericsnowcurrently-immortalize_empty_ke-3.12.0a7%2B-e472d94-vs-base.png)

