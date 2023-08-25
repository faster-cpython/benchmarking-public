# Results

- fork: faster-cpython
- version: 3.12.0a6+
- commit hash: [ed869aa](https://github.com/faster%2dcpython/cpython/commit/ed869aa)
- commit date: 2023-03-23T02:24:34+00:00
- commit merge base: [d49409196e0c73c38e3f96cf860cbffda40607ec](https://github.com/faster%2dcpython/cpython/commit/d49409196e0c73c38e3f96cf860cbffda40607ec)
- ref: no_predict

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4510595966)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230323-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a6%2B-ed869aa.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster \* (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230323-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a6%2B-ed869aa-vs-3.10.4.md)
- [plot](bm-20230323-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a6%2B-ed869aa-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster \* (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230323-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a6%2B-ed869aa-vs-3.11.0.md)
- [plot](bm-20230323-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a6%2B-ed869aa-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- [table](bm-20230323-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a6%2B-ed869aa-vs-base.md)
- [plot](bm-20230323-pythonperf1-amd64-faster%252dcpython-no_predict-3.12.0a6%2B-ed869aa-vs-base.png)

