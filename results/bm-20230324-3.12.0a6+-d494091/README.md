# Results

- fork: python
- version: 3.12.0a6+
- commit hash: [d494091](https://github.com/python/cpython/commit/d494091)
- commit date: 2023-03-24T00:39:12-05:00
- ref: d49409196e0c73c38e3f

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4991986140)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-67-generic-x86_64-with-glibc2.35
- [raw results](bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091.json)

### vs. 3.10.4

- 1.26x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.10.4.md)
- [plot](bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.10.4.png)

### vs. 3.11.0

- 1.05x faster
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
- [table](bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.11.0.md)
- [plot](bm-20230324-pythonperf2-x86_64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.11.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4510595966)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091.json)

### vs. 3.10.4

- 1.23x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.10.4.md)
- [plot](bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.10.4.png)

### vs. 3.11.0

- 1.11x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.11.0.md)
- [plot](bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6%2B-d494091-vs-3.11.0.png)

