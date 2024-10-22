# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [9315688](https://github.com/python/cpython/commit/9315688)
- commit date: 2024-07-03T10:18:34+01:00
- commit merge base: [51c4a324c037fb2e31640202243fd1c8b33800d5](https://github.com/python/cpython/commit/51c4a324c037fb2e31640202243fd1c8b33800d5)
- ref: 93156880efd14ad7adc7

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10009013368)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.10.4.md)
- [📈time plot](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 99.10%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.12.0.md)
- [📈time plot](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.13.0.md)
- [📈time plot](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.13.0b2.md)
- [📈time plot](bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688-vs-3.13.0b2.svg)

