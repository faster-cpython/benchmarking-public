# Results

- fork: brandtbucher
- version: 3.13.0a5+
- tier 2: False
- jit: True
- commit hash: [98575b4](https://github.com/brandtbucher/cpython/commit/98575b4)
- commit date: 2024-03-21T12:37:08-07:00
- commit merge base: [dcaf33a41d5d220523d71c9b35bc08f5b8405dac](https://github.com/brandtbucher/cpython/commit/dcaf33a41d5d220523d71c9b35bc08f5b8405dac)
- ref: justin_ghccc

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8381067358)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4.json)

### vs. 3.10.4

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.md)
- [📈time plot](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.14x slower (HPT: reliability of 65.23%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.md)
- [📈time plot](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.17x slower (HPT: reliability of 67.10%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.md)
- [📈time plot](bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5%2B-98575b4-vs-3.12.0.png)

