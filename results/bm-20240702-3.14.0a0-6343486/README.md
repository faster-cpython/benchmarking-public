# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [6343486](https://github.com/python/cpython/commit/6343486)
- commit date: 2024-07-02T16:27:51+05:30
- commit merge base: [15232a0819a2f7e0f448f28f2e6081912d10e7cb](https://github.com/python/cpython/commit/15232a0819a2f7e0f448f28f2e6081912d10e7cb)
- ref: 6343486eb60ac5a9e154

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9765724010)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.10.4.md)
- [📈time plot](bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.12.0.md)
- [📈time plot](bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9764247137)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.10.4.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 80.47%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.12.0.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9764250031)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486.json)

### vs. 3.10.4

- Geometric mean: 1.06x faster (HPT: reliability of 90.59%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.10.4.md)
- [📈time plot](bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.12.0.md)
- [📈time plot](bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-pythonperf1_win32-x86-python-6343486eb60ac5a9e154-3.14.0a0-6343486-vs-3.13.0b2.svg)

