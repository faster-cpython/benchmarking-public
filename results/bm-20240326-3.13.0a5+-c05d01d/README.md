# Results

- fork: faster-cpython
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [c05d01d](https://github.com/faster%2dcpython/cpython/commit/c05d01d)
- commit date: 2024-03-26T13:45:40+00:00
- commit merge base: [bf82f77957a31c3731b4ec470c406f5708ca9ba3](https://github.com/faster%2dcpython/cpython/commit/bf82f77957a31c3731b4ec470c406f5708ca9ba3)
- ref: inline_values

## linux x86_64 (azure)

- [pystats raw](bm-20240326-azure-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-pystats.json)
- [pystats table](bm-20240326-azure-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8437592533)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: django_template, djangocms, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.10.4.md)
- [📈time plot](bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: django_template, djangocms, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.11.0.md)
- [📈time plot](bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: django_template, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.12.0.md)
- [📈time plot](bm-20240326-linux-x86_64-faster%252dcpython-inline_values-3.13.0a5%2B-c05d01d-vs-3.12.0.png)

