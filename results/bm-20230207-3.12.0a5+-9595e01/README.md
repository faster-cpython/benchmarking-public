# Results

- fork: gvanrossum
- version: 3.12.0a5+
- commit hash: [9595e01](https://github.com/gvanrossum/cpython/commit/9595e01)
- commit date: 2023-02-07T20:04:44-08:00
- commit merge base: [a9f01448a99c6a2ae34d448806176f2df3a5b323](https://github.com/gvanrossum/cpython/commit/a9f01448a99c6a2ae34d448806176f2df3a5b323)
- ref: call_family

## linux x86_64 (linux)

- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01.json)

### vs. 3.10.4

- 1.30x faster \*
- missing benchmarks: comprehensions, dask, flaskblogging, pylint
- [table](bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-3.10.4.md)
- [plot](bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-3.10.4.png)

### vs. 3.11.0

- 1.04x faster \*
- missing benchmarks: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-3.11.0.md)
- [plot](bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-3.11.0.png)

### vs. base

- 1.00x slower
- [table](bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-base.md)
- [plot](bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5%2B-9595e01-vs-base.png)

