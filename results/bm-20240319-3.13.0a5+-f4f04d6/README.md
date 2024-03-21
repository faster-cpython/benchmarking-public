# Results

- fork: faster-cpython
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [f4f04d6](https://github.com/faster%2dcpython/cpython/commit/f4f04d6)
- commit date: 2024-03-19T11:51:52+00:00
- commit merge base: [039d20ae5428dfe3d70404d8a5297c70d41e2e2d](https://github.com/faster%2dcpython/cpython/commit/039d20ae5428dfe3d70404d8a5297c70d41e2e2d)
- ref: incremental_gc_3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8376604583)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-3.10.4.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.18x slower (HPT: reliability of 95.06%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-3.11.0.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.21x slower (HPT: reliability of 68.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-3.12.0.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.24x slower (HPT: reliability of 99.79%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-base-mem.png)
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-base.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-incremental_gc_3-3.13.0a5%2B-f4f04d6-vs-base.png)

