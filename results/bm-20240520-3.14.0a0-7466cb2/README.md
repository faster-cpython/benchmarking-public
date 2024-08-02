# Results

- fork: zooba
- version: 3.14.0a0
- config: 
- commit hash: [7466cb2](https://github.com/zooba/cpython/commit/7466cb2)
- commit date: 2024-05-20T19:34:18+01:00
- commit merge base: [caf6064a1bc15ac344afd78b780188e60b9c628e](https://github.com/zooba/cpython/commit/caf6064a1bc15ac344afd78b780188e60b9c628e)
- ref: cfg

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9163380409)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-3.10.4.md)
- [📈time plot](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 58.34%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-3.12.0.md)
- [📈time plot](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dulwich_log, mypy2
- [📄table](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-3.13.0b2.md)
- [📈time plot](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-base.md)
- [📈time plot](bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2-vs-base.svg)

