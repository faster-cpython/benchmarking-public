# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [a07cf4c](https://github.com/python/cpython/commit/a07cf4c)
- commit date: 2024-08-16T11:38:44+00:00
- commit merge base: [786cac0c64dc156dfee817e87f15ae56b7e3ed00](https://github.com/python/cpython/commit/786cac0c64dc156dfee817e87f15ae56b7e3ed00)
- ref: a07cf4ce25205d836a6b

## linux x86_64 (azure)

- [pystats raw](bm-20240816-azure-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-pystats.json)
- [pystats table](bm-20240816-azure-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10421396792)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.10.4.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 81.22%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.12.0.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.13.0.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.13.0b2.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c-vs-3.13.0b2.svg)

