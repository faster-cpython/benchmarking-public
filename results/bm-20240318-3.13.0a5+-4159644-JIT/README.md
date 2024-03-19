# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [4159644](https://github.com/python/cpython/commit/4159644)
- commit date: 2024-03-18T13:15:53-07:00
- commit merge base: [a9c304cf020e2fa3ae78fd88359dfc808c9dd639](https://github.com/python/cpython/commit/a9c304cf020e2fa3ae78fd88359dfc808c9dd639)
- ref: 415964417771946dcb7a

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8335669546)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5%2B-4159644.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5%2B-4159644-vs-3.10.4.md)
- [📈time plot](bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5%2B-4159644-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 58.65%, 1.00x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5%2B-4159644-vs-3.11.0.md)
- [📈time plot](bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5%2B-4159644-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 93.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5%2B-4159644-vs-3.12.0.md)
- [📈time plot](bm-20240318-linux-x86_64-python-415964417771946dcb7a-3.13.0a5%2B-4159644-vs-3.12.0.png)

