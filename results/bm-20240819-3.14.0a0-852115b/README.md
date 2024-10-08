# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [852115b](https://github.com/faster%2dcpython/cpython/commit/852115b)
- commit date: 2024-08-19T11:12:32+01:00
- commit merge base: [b9e10d1a0fc4d8428d4b36eb127570a832c26b6f](https://github.com/faster%2dcpython/cpython/commit/b9e10d1a0fc4d8428d4b36eb127570a832c26b6f)
- ref: specialize_call_ex

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10451579671)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-3.10.4.md)
- [📈time plot](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 67.69%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-3.12.0.md)
- [📈time plot](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-3.13.0b2.md)
- [📈time plot](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.94%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-base-mem.svg)
- [📄table](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-base.md)
- [📈time plot](bm-20240819-pythonperf2-x86_64-faster%252dcpython-specialize_call_ex-3.14.0a0-852115b-vs-base.svg)

