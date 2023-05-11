# Results

- fork: JelleZijlstra
- version: 3.12.0a7+
- commit hash: [827b9e5](https://github.com/JelleZijlstra/cpython/commit/827b9e5)
- commit date: 2023-05-02T19:13:32-07:00
- commit merge base: [872cbc613245db7a1fc5e6656ed0135d2e115f50](https://github.com/JelleZijlstra/cpython/commit/872cbc613245db7a1fc5e6656ed0135d2e115f50)
- ref: tvobject

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4882812781)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7%2B-827b9e5.json)

### vs. 3.10.4

- 1.27x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols
- [table](bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7%2B-827b9e5-vs-3.10.4.md)
- [plot](bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7%2B-827b9e5-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols
- [table](bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7%2B-827b9e5-vs-3.11.0.md)
- [plot](bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7%2B-827b9e5-vs-3.11.0.png)

### vs. base

- 1.01x faster
- [table](bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7%2B-827b9e5-vs-base.md)
- [plot](bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7%2B-827b9e5-vs-base.png)

