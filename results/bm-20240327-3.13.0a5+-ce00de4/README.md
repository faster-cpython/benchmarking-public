# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [ce00de4](https://github.com/python/cpython/commit/ce00de4)
- commit date: 2024-03-27T16:46:35+02:00
- commit merge base: [92397d5ead38dde4154e70d00f24973bcf2a925a](https://github.com/python/cpython/commit/92397d5ead38dde4154e70d00f24973bcf2a925a)
- ref: ce00de4c8cd39816f992

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8456354958)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.10.4.md)
- [📈time plot](bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.11.0.md)
- [📈time plot](bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.12.0.md)
- [📈time plot](bm-20240327-linux-x86_64-python-ce00de4c8cd39816f992-3.13.0a5%2B-ce00de4-vs-3.12.0.png)

