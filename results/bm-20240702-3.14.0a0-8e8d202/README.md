# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [8e8d202](https://github.com/python/cpython/commit/8e8d202)
- commit date: 2024-07-02T12:30:14-04:00
- commit merge base: [1ac273224a85126c4356e355f7445206fadde7ec](https://github.com/python/cpython/commit/1ac273224a85126c4356e355f7445206fadde7ec)
- ref: 8e8d202f552c993f4091

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9767741972)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202-vs-3.10.4.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 98.11%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202-vs-3.12.0.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202-vs-3.13.0b2.svg)

