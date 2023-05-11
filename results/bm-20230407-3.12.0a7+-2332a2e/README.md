# Results

- fork: ericsnowcurrently
- version: 3.12.0a7+
- commit hash: [2332a2e](https://github.com/ericsnowcurrently/cpython/commit/2332a2e)
- commit date: 2023-04-07T12:18:52-06:00
- commit merge base: [52bc2e7b9d451821513a580a9b73c20cfdcf2b21](https://github.com/ericsnowcurrently/cpython/commit/52bc2e7b9d451821513a580a9b73c20cfdcf2b21)
- ref: tstate_current_as_th

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4671551840)
- cpu model: missing
- platform: Windows-11-10.0.22000-SP0
- [raw results](bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e.json)

### vs. 3.10.4

- 1.17x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.10.4.md)
- [plot](bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.10.4.png)

### vs. 3.11.0

- 1.06x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
- [table](bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.11.0.md)
- [plot](bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.11.0.png)

### vs. base

- 1.02x slower
- [table](bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-base.md)
- [plot](bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-base.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4799659871)
- cpu model: missing
- platform: macOS-13.2.1-arm64-arm-64bit
- [raw results](bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e.json)

### vs. 3.10.4

- 1.17x faster \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.10.4.md)
- [plot](bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x slower \*
- missing benchmarks: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
- new benchmarks: dask
- [table](bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.11.0.md)
- [plot](bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-3.11.0.png)

### vs. base

- 1.03x slower
- [table](bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-base.md)
- [plot](bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-2332a2e-vs-base.png)

