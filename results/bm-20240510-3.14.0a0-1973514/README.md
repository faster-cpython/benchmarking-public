# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [1973514](https://github.com/faster%2dcpython/cpython/commit/1973514)
- commit date: 2024-05-10T16:37:09+01:00
- commit merge base: [35b5eaa176a5bae8a0cacb9c9f40ec948ecc4325](https://github.com/faster%2dcpython/cpython/commit/35b5eaa176a5bae8a0cacb9c9f40ec948ecc4325)
- ref: test_perf_jit

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9034646637)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-3.10.4.md)
- [📈time plot](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 99.72%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-3.12.0.md)
- [📈time plot](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 99.32%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-3.13.0b2.md)
- [📈time plot](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-base-mem.svg)
- [📄table](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-base.md)
- [📈time plot](bm-20240510-linux-x86_64-faster%252dcpython-test_perf_jit-3.14.0a0-1973514-vs-base.svg)

