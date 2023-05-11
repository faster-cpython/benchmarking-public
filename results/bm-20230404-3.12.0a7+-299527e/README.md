# Results

- fork: ericsnowcurrently
- version: 3.12.0a7+
- commit hash: [299527e](https://github.com/ericsnowcurrently/cpython/commit/299527e)
- commit date: 2023-04-04T17:14:01-06:00
- commit merge base: [f513d5c80672c76acbdaf7d5b601f4bbe9fae56a](https://github.com/ericsnowcurrently/cpython/commit/f513d5c80672c76acbdaf7d5b601f4bbe9fae56a)
- ref: per_interpreter_allo

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4613186413)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e.json)

### vs. 3.10.4

- 1.28x faster
- missing benchmarks: flaskblogging, pylint
- [table](bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-3.10.4.md)
- [plot](bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-3.10.4.png)

### vs. 3.11.0

- 1.02x faster \*
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-3.11.0.md)
- [plot](bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-base.md)
- [plot](bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7%2B-299527e-vs-base.png)

