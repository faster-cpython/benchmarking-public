# Results

- fork: faster-cpython
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [8183250](https://github.com/faster%2dcpython/cpython/commit/8183250)
- commit date: 2024-03-27T09:05:24+00:00
- commit merge base: [bf82f77957a31c3731b4ec470c406f5708ca9ba3](https://github.com/faster%2dcpython/cpython/commit/bf82f77957a31c3731b4ec470c406f5708ca9ba3)
- ref: specialize_binary_op

## linux x86_64 (azure)

- [pystats raw](bm-20240327-azure-x86_64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-pystats.json)
- [pystats table](bm-20240327-azure-x86_64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-pystats.md)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8449221311)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.10.4.md)
- [📈time plot](bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.11.0.md)
- [📈time plot](bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.12.0.md)
- [📈time plot](bm-20240327-pythonperf1-amd64-faster%252dcpython-specialize_binary_op-3.13.0a5%2B-8183250-vs-3.12.0.png)

