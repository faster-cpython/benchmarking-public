# Results

- fork: ericsnowcurrently
- version: 3.12.0a7+
- commit hash: [d43bb5f](https://github.com/ericsnowcurrently/cpython/commit/d43bb5f)
- commit date: 2023-04-10T15:19:52-06:00
- commit merge base: [5d7d86f2fdbbfc23325e7256ee289bf20ce7124e](https://github.com/ericsnowcurrently/cpython/commit/5d7d86f2fdbbfc23325e7256ee289bf20ce7124e)
- ref: per_interpreter_gil_

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4669710692)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-d43bb5f.json)

### vs. 3.10.4

- 1.30x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-d43bb5f-vs-3.10.4.md)
- [plot](bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-d43bb5f-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-d43bb5f-vs-3.11.0.md)
- [plot](bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-d43bb5f-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-d43bb5f-vs-base.md)
- [plot](bm-20230410-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7%2B-d43bb5f-vs-base.png)

