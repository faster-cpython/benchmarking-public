# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [b9e10d1](https://github.com/python/cpython/commit/b9e10d1)
- commit date: 2024-08-19T07:51:38+00:00
- commit merge base: [be257c58152e9b960827362b11c9ef2223fd6267](https://github.com/python/cpython/commit/be257c58152e9b960827362b11c9ef2223fd6267)
- ref: b9e10d1a0fc4d8428d4b, main

## linux x86_64 (azure)

- [pystats raw](bm-20240819-azure-x86_64-python-main-3.14.0a0-b9e10d1-pystats.json)
- [pystats table](bm-20240819-azure-x86_64-python-main-3.14.0a0-b9e10d1-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10451284514)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1-vs-3.10.4.md)
- [📈time plot](bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1-vs-3.12.0.md)
- [📈time plot](bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1-vs-3.13.0b2.md)
- [📈time plot](bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10451579671)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.10.4.md)
- [📈time plot](bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 84.03%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.12.0.md)
- [📈time plot](bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.13.0b2.md)
- [📈time plot](bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1-vs-3.13.0b2.svg)

