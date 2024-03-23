# Results

- fork: gvanrossum
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [e6480f7](https://github.com/gvanrossum/cpython/commit/e6480f7)
- commit date: 2024-03-22T18:26:15-07:00
- commit merge base: [72eea512b88f8fd68b7258242c37da963ad87360](https://github.com/gvanrossum/cpython/commit/72eea512b88f8fd68b7258242c37da963ad87360)
- ref: e6480f74cbec3ae4fb55

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8398451474)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-3.10.4.md)
- [📈time plot](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 65.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-3.11.0.md)
- [📈time plot](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 97.15%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-3.12.0.md)
- [📈time plot](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 92.65%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-base-mem.png)
- [📄table](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-base.md)
- [📈time plot](bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5%2B-e6480f7-vs-base.png)

