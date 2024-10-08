# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [43a18d0](https://github.com/mdboom/cpython/commit/43a18d0)
- commit date: 2024-07-19T11:22:08-04:00
- commit merge base: [d66b06107b0104af513f664d9a5763216639018b](https://github.com/mdboom/cpython/commit/d66b06107b0104af513f664d9a5763216639018b)
- ref: no_additional_schedu

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10010861102)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-3.10.4.md)
- [📈time plot](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 97.65%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-3.12.0.md)
- [📈time plot](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-3.13.0b2.md)
- [📈time plot](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-base.md)
- [📈time plot](bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0-vs-base.svg)

