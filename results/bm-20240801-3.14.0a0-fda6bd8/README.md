# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [fda6bd8](https://github.com/python/cpython/commit/fda6bd8)
- commit date: 2024-08-01T14:12:33+02:00
- commit merge base: [88030861e216ac791725c8784752201d6fe31329](https://github.com/python/cpython/commit/88030861e216ac791725c8784752201d6fe31329)
- ref: fda6bd842a2b93a50152

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10532580498)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.10.4.md)
- [📈time plot](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.12.0.md)
- [📈time plot](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 93.30%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.13.0.md)
- [📈time plot](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-linux-x86_64-python-fda6bd842a2b93a50152-3.14.0a0-fda6bd8-vs-3.13.0b2.svg)

