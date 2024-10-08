# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [db6f5e1](https://github.com/python/cpython/commit/db6f5e1)
- commit date: 2024-08-13T15:30:59+01:00
- commit merge base: [7a65439b93d6ee4d4e32757b55909b882f9a2056](https://github.com/python/cpython/commit/7a65439b93d6ee4d4e32757b55909b882f9a2056)
- ref: db6f5e193315a3bbfa7b

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10453425857)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json)

### vs. 3.10.4

- Geometric mean: 1.22x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.10.4.md)
- [📈time plot](bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.56x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.12.0.md)
- [📈time plot](bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.58x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.13.0b2.md)
- [📈time plot](bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10453425857)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json)

### vs. 3.10.4

- Geometric mean: 1.05x slower (HPT: reliability of 99.83%, 1.01x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.10.4.md)
- [📈time plot](bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.12.0.md)
- [📈time plot](bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.41x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.13.0b2.md)
- [📈time plot](bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10453425857)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json)

### vs. 3.10.4

- Geometric mean: 1.11x slower (HPT: reliability of 99.99%, 1.06x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.10.4.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.12.0.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.13.0b2.md)
- [📈time plot](bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1-vs-3.13.0b2.svg)

