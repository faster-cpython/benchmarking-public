# Results

- fork: faster-cpython
- version: 3.12.0a5+
- commit hash: [d579d2e](https://github.com/faster%2dcpython/cpython/commit/d579d2e)
- commit date: 2023-02-23T13:14:05+00:00
- commit merge base: [22b8d77b98a5944e688be0927b8139c49d4a7257](https://github.com/faster%2dcpython/cpython/commit/22b8d77b98a5944e688be0927b8139c49d4a7257)
- ref: pep_669

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/4253128438)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-122-generic-x86_64-with-glibc2.31
- [raw results](bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster \* (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-3.10.4.md)
- [plot](bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster \* (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- missing benchmarks: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols
- [table](bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-3.11.0.md)
- [plot](bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-3.11.0.png)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- [table](bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-base.md)
- [plot](bm-20230223-linux-x86_64-faster%252dcpython-pep_669-3.12.0a5%2B-d579d2e-vs-base.png)

