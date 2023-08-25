# Results

- fork: python
- version: 3.12.0a6+
- commit hash: [7f760c2](https://github.com/python/cpython/commit/7f760c2)
- commit date: 2023-03-21T11:08:46+00:00
- ref: 7f760c2fca3dc5f46a51

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4481694268)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230321-linux-x86_64-python-7f760c2fca3dc5f46a51-3.12.0a6%2B-7f760c2.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster \* (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230321-linux-x86_64-python-7f760c2fca3dc5f46a51-3.12.0a6%2B-7f760c2-vs-3.10.4.md)
- [plot](bm-20230321-linux-x86_64-python-7f760c2fca3dc5f46a51-3.12.0a6%2B-7f760c2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230321-linux-x86_64-python-7f760c2fca3dc5f46a51-3.12.0a6%2B-7f760c2-vs-3.11.0.md)
- [plot](bm-20230321-linux-x86_64-python-7f760c2fca3dc5f46a51-3.12.0a6%2B-7f760c2-vs-3.11.0.png)

