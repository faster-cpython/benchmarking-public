# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [325e9b8](https://github.com/python/cpython/commit/325e9b8)
- commit date: 2024-08-13T21:42:19+00:00
- commit merge base: [ee1b8ce26e700350e47a5f65201097121c41912e](https://github.com/python/cpython/commit/ee1b8ce26e700350e47a5f65201097121c41912e)
- ref: 325e9b8ef400b86fb077

## linux x86_64 (azure)

- [pystats raw](bm-20240813-azure-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-pystats.json)
- [pystats table](bm-20240813-azure-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10378642008)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-vs-3.10.4.md)
- [📈time plot](bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-vs-3.12.0.md)
- [📈time plot](bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-vs-3.13.0b2.md)
- [📈time plot](bm-20240813-linux-x86_64-python-325e9b8ef400b86fb077-3.14.0a0-325e9b8-vs-3.13.0b2.svg)

