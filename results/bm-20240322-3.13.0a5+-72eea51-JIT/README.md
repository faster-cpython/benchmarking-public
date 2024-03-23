# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [72eea51](https://github.com/python/cpython/commit/72eea51)
- commit date: 2024-03-22T19:14:09+00:00
- commit merge base: [e28477f214276db941e715eebc8cdfb96c1207d9](https://github.com/python/cpython/commit/e28477f214276db941e715eebc8cdfb96c1207d9)
- ref: 72eea512b88f8fd68b72

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8398451474)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5%2B-72eea51.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5%2B-72eea51-vs-3.10.4.md)
- [📈time plot](bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5%2B-72eea51-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x faster (HPT: reliability of 61.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5%2B-72eea51-vs-3.11.0.md)
- [📈time plot](bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5%2B-72eea51-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 72.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5%2B-72eea51-vs-3.12.0.md)
- [📈time plot](bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5%2B-72eea51-vs-3.12.0.png)

