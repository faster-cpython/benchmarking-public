# Results

- fork: mdboom
- version: 3.12.0a7+
- commit hash: [b488f91](https://github.com/mdboom/cpython/commit/b488f91)
- commit date: 2023-05-05T10:17:55-04:00
- commit merge base: [45a9e3834a6ed20ee250e2e5a8583dffcef0eb73](https://github.com/mdboom/cpython/commit/45a9e3834a6ed20ee250e2e5a8583dffcef0eb73)
- ref: bolt_experiment

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4897599938)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7%2B-b488f91.json)

### vs. 3.10.4

- 1.24x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7%2B-b488f91-vs-3.10.4.md)
- [plot](bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7%2B-b488f91-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols
- [table](bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7%2B-b488f91-vs-3.11.0.md)
- [plot](bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7%2B-b488f91-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7%2B-b488f91-vs-base.md)
- [plot](bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7%2B-b488f91-vs-base.png)

