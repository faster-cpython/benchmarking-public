# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [dd0ee20](https://github.com/python/cpython/commit/dd0ee20)
- commit date: 2024-10-10T21:26:01+01:00
- commit merge base: [427dcf24de4e06d239745d74d08c4b2e541dca5a](https://github.com/python/cpython/commit/427dcf24de4e06d239745d74d08c4b2e541dca5a)
- ref: main

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11281869816)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20.json)

### vs. 3.10.4

- Geometric mean: 1.02x faster (HPT: reliability of 88.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20-vs-3.10.4.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.14x slower (HPT: reliability of 99.99%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20-vs-3.12.0.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.20x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20-vs-3.13.0b2.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-python-main-3.14.0a0-dd0ee20-vs-3.13.0b2.svg)

