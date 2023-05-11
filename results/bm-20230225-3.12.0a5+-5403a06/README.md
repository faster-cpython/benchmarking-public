# Results

- fork: faster-cpython
- version: 3.12.0a5+
- commit hash: [5403a06](https://github.com/faster%2dcpython/cpython/commit/5403a06)
- commit date: 2023-02-25T13:12:58+00:00
- commit merge base: [1fa38906f0b228e6b0a6baa89ab6316989b0388a](https://github.com/faster%2dcpython/cpython/commit/1fa38906f0b228e6b0a6baa89ab6316989b0388a)
- ref: no_small_ints

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4270190713)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230225-linux-x86_64-faster%252dcpython-no_small_ints-3.12.0a5%2B-5403a06.json)

### vs. 3.10.4

- 1.29x faster \*
- missing benchmarks: comprehensions, flaskblogging, pylint
- [table](bm-20230225-linux-x86_64-faster%252dcpython-no_small_ints-3.12.0a5%2B-5403a06-vs-3.10.4.md)
- [plot](bm-20230225-linux-x86_64-faster%252dcpython-no_small_ints-3.12.0a5%2B-5403a06-vs-3.10.4.png)

### vs. 3.11.0

- 1.03x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230225-linux-x86_64-faster%252dcpython-no_small_ints-3.12.0a5%2B-5403a06-vs-3.11.0.md)
- [plot](bm-20230225-linux-x86_64-faster%252dcpython-no_small_ints-3.12.0a5%2B-5403a06-vs-3.11.0.png)

### vs. base

- 1.01x slower
- [table](bm-20230225-linux-x86_64-faster%252dcpython-no_small_ints-3.12.0a5%2B-5403a06-vs-base.md)
- [plot](bm-20230225-linux-x86_64-faster%252dcpython-no_small_ints-3.12.0a5%2B-5403a06-vs-base.png)

