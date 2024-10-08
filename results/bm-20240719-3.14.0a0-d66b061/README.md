# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [d66b061](https://github.com/python/cpython/commit/d66b061)
- commit date: 2024-07-19T16:47:10+02:00
- commit merge base: [a1df1b44394784721239615f307b273455536d14](https://github.com/python/cpython/commit/a1df1b44394784721239615f307b273455536d14)
- ref: d66b06107b0104af513f

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10010857522)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061-vs-3.10.4.md)
- [📈time plot](bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 51.15%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061-vs-3.12.0.md)
- [📈time plot](bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061-vs-3.13.0b2.md)
- [📈time plot](bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061-vs-3.13.0b2.svg)

