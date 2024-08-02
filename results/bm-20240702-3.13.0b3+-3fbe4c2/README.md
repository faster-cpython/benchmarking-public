# Results

- fork: mdboom
- version: 3.13.0b3+
- config: 
- commit hash: [3fbe4c2](https://github.com/mdboom/cpython/commit/3fbe4c2)
- commit date: 2024-07-02T17:36:33-04:00
- ref: remove_pragma_313

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9768323837)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3%2B-3fbe4c2.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3%2B-3fbe4c2-vs-3.10.4.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3%2B-3fbe4c2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3%2B-3fbe4c2-vs-3.12.0.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3%2B-3fbe4c2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3%2B-3fbe4c2-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3%2B-3fbe4c2-vs-3.13.0b2.svg)

