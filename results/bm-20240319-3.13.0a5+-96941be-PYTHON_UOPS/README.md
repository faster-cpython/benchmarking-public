# Results

- fork: faster-cpython
- version: 3.13.0a5+
- tier 2: True
- jit: False
- commit hash: [96941be](https://github.com/faster%2dcpython/cpython/commit/96941be)
- commit date: 2024-03-19T11:47:32+00:00
- commit merge base: [0f278012e88fa9607d85bc6c7265fd394f0ac163](https://github.com/faster%2dcpython/cpython/commit/0f278012e88fa9607d85bc6c7265fd394f0ac163)
- ref: tier2_hot_cold_split

## linux x86_64 (azure)

- [pystats raw](bm-20240319-azure-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-pystats.json)
- [pystats table](bm-20240319-azure-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-pystats.md)

### vs. base

- [pystats diff](bm-20240319-azure-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8342515240)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.35
- [raw results](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-3.10.4.md)
- [📈time plot](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-3.11.0.md)
- [📈time plot](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-3.12.0.md)
- [📈time plot](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-base-mem.png)
- [📄table](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-base.md)
- [📈time plot](bm-20240319-pythonperf2-x86_64-faster%252dcpython-tier2_hot_cold_split-3.13.0a5%2B-96941be-vs-base.png)

