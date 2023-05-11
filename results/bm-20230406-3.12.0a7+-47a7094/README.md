# Results

- fork: ericsnowcurrently
- version: 3.12.0a7+
- commit hash: [47a7094](https://github.com/ericsnowcurrently/cpython/commit/47a7094)
- commit date: 2023-04-06T16:03:28-06:00
- commit merge base: [52bc2e7b9d451821513a580a9b73c20cfdcf2b21](https://github.com/ericsnowcurrently/cpython/commit/52bc2e7b9d451821513a580a9b73c20cfdcf2b21)
- ref: tstate_current_as_th

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4634397966)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094.json)

### vs. 3.10.4

- 1.31x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.10.4.md)
- [plot](bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.11.0.md)
- [plot](bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-3.11.0.png)

### vs. base

- 1.00x faster
- [table](bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-base.md)
- [plot](bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7%2B-47a7094-vs-base.png)

