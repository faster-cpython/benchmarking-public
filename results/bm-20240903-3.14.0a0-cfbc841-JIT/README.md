# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [cfbc841](https://github.com/python/cpython/commit/cfbc841)
- commit date: 2024-09-03T22:52:00+03:00
- commit merge base: [68fe5758bf1900ffdcdf7cd9e40f5018555a39d4](https://github.com/python/cpython/commit/68fe5758bf1900ffdcdf7cd9e40f5018555a39d4)
- ref: cfbc841ef3c27b3e65d1

## linux x86_64 (azure)

- [pystats raw](bm-20240903-azure-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-pystats.json)
- [pystats table](bm-20240903-azure-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10726580133)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-vs-3.10.4.md)
- [📈time plot](bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-vs-3.12.0.md)
- [📈time plot](bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-vs-3.13.0b2.md)
- [📈time plot](bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841-vs-3.13.0b2.svg)

