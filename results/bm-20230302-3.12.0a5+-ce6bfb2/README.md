# Results

- fork: faster-cpython
- version: 3.12.0a5+
- commit hash: [ce6bfb2](https://github.com/faster%2dcpython/cpython/commit/ce6bfb2)
- commit date: 2023-03-02T17:06:15+00:00
- commit merge base: [4c87537efb5fd28b4e4ee9631076ed5953720156](https://github.com/faster%2dcpython/cpython/commit/4c87537efb5fd28b4e4ee9631076ed5953720156)
- ref: long_rearrange_size_

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4316443260)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230302-linux-x86_64-faster%252dcpython-long_rearrange_size_-3.12.0a5%2B-ce6bfb2.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster \* (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230302-linux-x86_64-faster%252dcpython-long_rearrange_size_-3.12.0a5%2B-ce6bfb2-vs-3.10.4.md)
- [plot](bm-20230302-linux-x86_64-faster%252dcpython-long_rearrange_size_-3.12.0a5%2B-ce6bfb2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster \* (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230302-linux-x86_64-faster%252dcpython-long_rearrange_size_-3.12.0a5%2B-ce6bfb2-vs-3.11.0.md)
- [plot](bm-20230302-linux-x86_64-faster%252dcpython-long_rearrange_size_-3.12.0a5%2B-ce6bfb2-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 98.58%, 1.00x faster at 99th %ile)
- [table](bm-20230302-linux-x86_64-faster%252dcpython-long_rearrange_size_-3.12.0a5%2B-ce6bfb2-vs-base.md)
- [plot](bm-20230302-linux-x86_64-faster%252dcpython-long_rearrange_size_-3.12.0a5%2B-ce6bfb2-vs-base.png)

