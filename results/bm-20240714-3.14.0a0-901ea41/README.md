# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [901ea41](https://github.com/python/cpython/commit/901ea41)
- commit date: 2024-07-14T10:08:47+02:00
- commit merge base: [a2bec77d25b11f50362a7117223f6d1d5029a909](https://github.com/python/cpython/commit/a2bec77d25b11f50362a7117223f6d1d5029a909)
- ref: 901ea411bf51f59f2a4b

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9992192480)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.10.4.md)
- [📈time plot](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.12.0.md)
- [📈time plot](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.13.0.md)
- [📈time plot](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 76.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-base-mem.svg)
- [📄table](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-base.md)
- [📈time plot](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.13.0b2.md)
- [📈time plot](bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41-vs-3.13.0b2.svg)

