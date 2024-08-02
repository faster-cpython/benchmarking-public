# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [a03affd](https://github.com/mdboom/cpython/commit/a03affd)
- commit date: 2024-07-02T16:44:41-04:00
- commit merge base: [8e8d202f552c993f40913b628139a39a5abe6a03](https://github.com/mdboom/cpython/commit/8e8d202f552c993f40913b628139a39a5abe6a03)
- ref: remove_pragma

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9767741972)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-3.10.4.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.34%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-3.12.0.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 98.65%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-base.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd-vs-base.svg)

