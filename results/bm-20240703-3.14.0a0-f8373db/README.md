# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [f8373db](https://github.com/python/cpython/commit/f8373db)
- commit date: 2024-07-03T18:36:57+02:00
- commit merge base: [7c66906802cd8534b05264bd47acf9eb9db6d09e](https://github.com/python/cpython/commit/7c66906802cd8534b05264bd47acf9eb9db6d09e)
- ref: main

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9781018205)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db-vs-3.10.4.md)
- [📈time plot](bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db-vs-3.12.0.md)
- [📈time plot](bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db-vs-3.13.0b2.md)
- [📈time plot](bm-20240703-pythonperf1-amd64-python-main-3.14.0a0-f8373db-vs-3.13.0b2.svg)

