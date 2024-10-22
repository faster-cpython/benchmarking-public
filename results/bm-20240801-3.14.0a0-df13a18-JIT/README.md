# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [df13a18](https://github.com/python/cpython/commit/df13a18)
- commit date: 2024-08-01T16:19:05-07:00
- commit merge base: [fda6bd842a2b93a501526f1b830eb900d935ac73](https://github.com/python/cpython/commit/fda6bd842a2b93a501526f1b830eb900d935ac73)
- ref: df13a1821a90fcfb75ec

## linux x86_64 (azure)

- [pystats raw](bm-20240801-azure-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-pystats.json)
- [pystats table](bm-20240801-azure-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10207463718)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.10.4.md)
- [📈time plot](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.12.0.md)
- [📈time plot](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 75.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.13.0.md)
- [📈time plot](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.13.0b2.md)
- [📈time plot](bm-20240801-linux-x86_64-python-df13a1821a90fcfb75ec-3.14.0a0-df13a18-vs-3.13.0b2.svg)

