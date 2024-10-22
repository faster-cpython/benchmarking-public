# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [10855bc](https://github.com/faster%2dcpython/cpython/commit/10855bc)
- commit date: 2024-08-22T16:46:44+01:00
- commit merge base: [297f2e093ec95800ae2184330b8408c875523467](https://github.com/faster%2dcpython/cpython/commit/297f2e093ec95800ae2184330b8408c875523467)
- ref: fix_not_specialized_

## linux x86_64 (azure)

- [pystats raw](bm-20240822-azure-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-pystats.json)
- [pystats table](bm-20240822-azure-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10511423628)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.10.4.md)
- [📈time plot](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 64.17%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.12.0.md)
- [📈time plot](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.13.0.md)
- [📈time plot](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.13.0b2.md)
- [📈time plot](bm-20240822-pythonperf2-x86_64-faster%252dcpython-fix_not_specialized_-3.14.0a0-10855bc-vs-3.13.0b2.svg)

