# Results

- fork: brandtbucher
- version: 3.12.0a7+
- commit hash: [7f90633](https://github.com/brandtbucher/cpython/commit/7f90633)
- commit date: 2023-04-28T23:57:53-07:00
- commit merge base: [738c226786997262b76557d2dadd2beb89ea3fd1](https://github.com/brandtbucher/cpython/commit/738c226786997262b76557d2dadd2beb89ea3fd1)
- ref: immortal_interpreter

## linux x86_64 (azure)

- [pystats raw](bm-20230428-azure-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-pystats.json)
- [pystats table](bm-20230428-azure-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4837501205)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633.json)

### vs. 3.10.4

- 1.24x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols
- [table](bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-vs-3.10.4.md)
- [plot](bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-vs-3.10.4.png)

### vs. 3.11.0

- 1.01x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols
- [table](bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-vs-3.11.0.md)
- [plot](bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-vs-base.md)
- [plot](bm-20230428-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7%2B-7f90633-vs-base.png)

