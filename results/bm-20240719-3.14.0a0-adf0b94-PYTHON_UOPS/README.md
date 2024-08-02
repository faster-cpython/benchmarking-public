# Results

- fork: python
- version: 3.14.0a0
- config: T2
- commit hash: [adf0b94](https://github.com/python/cpython/commit/adf0b94)
- commit date: 2024-07-19T10:16:59+01:00
- commit merge base: [1a0c7b9ba48a2dffb70bb0c7327abae1d3e87356](https://github.com/python/cpython/commit/1a0c7b9ba48a2dffb70bb0c7327abae1d3e87356)
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20240719-azure-x86_64-python-main-3.14.0a0-adf0b94-pystats.json)
- [pystats table](bm-20240719-azure-x86_64-python-main-3.14.0a0-adf0b94-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10006403389)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94-vs-3.10.4.md)
- [📈time plot](bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94-vs-3.12.0.md)
- [📈time plot](bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94-vs-3.13.0b2.md)
- [📈time plot](bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94-vs-3.13.0b2.svg)

