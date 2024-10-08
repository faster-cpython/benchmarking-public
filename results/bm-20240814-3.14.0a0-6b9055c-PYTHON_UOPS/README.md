# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: T2
- commit hash: [6b9055c](https://github.com/faster%2dcpython/cpython/commit/6b9055c)
- commit date: 2024-08-14T10:42:25+01:00
- commit merge base: [7a65439b93d6ee4d4e32757b55909b882f9a2056](https://github.com/faster%2dcpython/cpython/commit/7a65439b93d6ee4d4e32757b55909b882f9a2056)
- ref: specialize_call_kw

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10385273001)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-3.10.4.md)
- [📈time plot](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-3.12.0.md)
- [📈time plot](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-3.13.0b2.md)
- [📈time plot](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 63.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-base-mem.svg)
- [📄table](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-base.md)
- [📈time plot](bm-20240814-pythonperf2-x86_64-faster%252dcpython-specialize_call_kw-3.14.0a0-6b9055c-vs-base.svg)

