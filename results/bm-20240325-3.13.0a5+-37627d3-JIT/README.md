# Results

- fork: faster-cpython
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [37627d3](https://github.com/faster%2dcpython/cpython/commit/37627d3)
- commit date: 2024-03-25T17:23:27+00:00
- commit merge base: [507896d97dcff2d7999efa264b29d9003c525c49](https://github.com/faster%2dcpython/cpython/commit/507896d97dcff2d7999efa264b29d9003c525c49)
- ref: tier2_hot_cold_split

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8424439181)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.10.4.md)
- [📈time plot](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x faster (HPT: reliability of 67.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.11.0.md)
- [📈time plot](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 83.63%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.12.0.md)
- [📈time plot](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 66.48%, 1.00x faster at 99th %ile)
- Memory usage: 0.95x
- [🧠memory plot](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-base-mem.png)
- [📄table](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-base.md)
- [📈time plot](bm-20240325-linux-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-37627d3-vs-base.png)

