# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: JIT
- commit hash: [1b65c46](https://github.com/faster%2dcpython/cpython/commit/1b65c46)
- commit date: 2024-08-01T16:53:55+01:00
- commit merge base: [a9d56e38a08ec198a2289d8fff65444b39dd4a32](https://github.com/faster%2dcpython/cpython/commit/a9d56e38a08ec198a2289d8fff65444b39dd4a32)
- ref: monitoring_branch_ta

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10201187273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.10.4.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 85.51%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.12.0.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x faster (HPT: reliability of 99.63%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.13.0.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 63.82%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-base.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-pythonperf1-amd64-faster%252dcpython-monitoring_branch_ta-3.14.0a0-1b65c46-vs-3.13.0b2.svg)

