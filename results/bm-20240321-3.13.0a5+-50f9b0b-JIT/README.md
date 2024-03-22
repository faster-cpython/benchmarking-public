# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [50f9b0b](https://github.com/python/cpython/commit/50f9b0b)
- commit date: 2024-03-21T22:17:09+00:00
- commit merge base: [0907871d43bffb613cbd560224e1a9db13d06c06](https://github.com/python/cpython/commit/0907871d43bffb613cbd560224e1a9db13d06c06)
- ref: 50f9b0b1e0fb18187575

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8384069642)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5%2B-50f9b0b.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5%2B-50f9b0b-vs-3.10.4.md)
- [📈time plot](bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5%2B-50f9b0b-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.22x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5%2B-50f9b0b-vs-3.11.0.md)
- [📈time plot](bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5%2B-50f9b0b-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.25x slower (HPT: reliability of 99.96%, 1.01x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5%2B-50f9b0b-vs-3.12.0.md)
- [📈time plot](bm-20240321-linux-x86_64-python-50f9b0b1e0fb18187575-3.13.0a5%2B-50f9b0b-vs-3.12.0.png)

