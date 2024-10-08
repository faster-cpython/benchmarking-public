# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [bb1d303](https://github.com/python/cpython/commit/bb1d303)
- commit date: 2024-08-20T16:52:58+01:00
- commit merge base: [bffed80230f2617de2ee02bd4bdded1024234dab](https://github.com/python/cpython/commit/bffed80230f2617de2ee02bd4bdded1024234dab)
- ref: bb1d30336e83837d4191

## linux x86_64 (azure)

- [pystats raw](bm-20240820-azure-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-pystats.json)
- [pystats table](bm-20240820-azure-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10476243521)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-vs-3.10.4.md)
- [📈time plot](bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 72.11%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-vs-3.12.0.md)
- [📈time plot](bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-vs-3.13.0b2.md)
- [📈time plot](bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303-vs-3.13.0b2.svg)

