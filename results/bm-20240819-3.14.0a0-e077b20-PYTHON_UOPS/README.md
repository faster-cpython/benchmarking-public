# Results

- fork: python
- version: 3.14.0a0
- config: T2
- commit hash: [e077b20](https://github.com/python/cpython/commit/e077b20)
- commit date: 2024-08-19T11:49:42+01:00
- commit merge base: [b9e10d1a0fc4d8428d4b36eb127570a832c26b6f](https://github.com/python/cpython/commit/b9e10d1a0fc4d8428d4b36eb127570a832c26b6f)
- ref: e077b201f49a6007ddad

## linux x86_64 (azure)

- [pystats raw](bm-20240819-azure-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-pystats.json)
- [pystats table](bm-20240819-azure-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10454522176)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 64.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-vs-3.10.4.md)
- [📈time plot](bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-vs-3.12.0.md)
- [📈time plot](bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.24x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-vs-3.13.0b2.md)
- [📈time plot](bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20-vs-3.13.0b2.svg)

