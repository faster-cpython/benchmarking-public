# Results

- fork: faster-cpython
- version: 3.13.0a5+
- tier 2: True
- jit: False
- commit hash: [f012ce0](https://github.com/faster%2dcpython/cpython/commit/f012ce0)
- commit date: 2024-03-19T14:52:13+00:00
- commit merge base: [0f278012e88fa9607d85bc6c7265fd394f0ac163](https://github.com/faster%2dcpython/cpython/commit/0f278012e88fa9607d85bc6c7265fd394f0ac163)
- ref: optimizer_trim_trace

## linux x86_64 (azure)

- [pystats raw](bm-20240319-azure-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-pystats.json)
- [pystats table](bm-20240319-azure-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-pystats.md)

### vs. base

- [pystats diff](bm-20240319-azure-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8345202002)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-3.10.4.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-3.11.0.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-3.12.0.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-base-mem.png)
- [📄table](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-base.md)
- [📈time plot](bm-20240319-linux-x86_64-faster%252dcpython-optimizer_trim_trace-3.13.0a5%2B-f012ce0-vs-base.png)

