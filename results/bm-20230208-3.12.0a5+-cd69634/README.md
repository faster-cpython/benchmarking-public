# Results

- fork: gvanrossum
- version: 3.12.0a5+
- commit hash: [cd69634](https://github.com/gvanrossum/cpython/commit/cd69634)
- commit date: 2023-02-08T07:19:49-08:00
- commit merge base: [a9f01448a99c6a2ae34d448806176f2df3a5b323](https://github.com/gvanrossum/cpython/commit/a9f01448a99c6a2ae34d448806176f2df3a5b323)
- ref: call_family

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [pystats raw](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-pystats.json)
- [pystats table](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-pystats.md)
- [raw results](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: comprehensions, dask, flaskblogging, pylint
- [table](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-3.10.4.md)
- [plot](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-3.11.0.md)
- [plot](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-base.md)
- [plot](bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-cd69634-vs-base.png)

