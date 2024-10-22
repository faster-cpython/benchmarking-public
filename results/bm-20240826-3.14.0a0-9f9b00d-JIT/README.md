# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [9f9b00d](https://github.com/python/cpython/commit/9f9b00d)
- commit date: 2024-08-26T19:27:22+00:00
- commit merge base: [1eed0f968f5f44d6a13403c1676298a322cbfbad](https://github.com/python/cpython/commit/1eed0f968f5f44d6a13403c1676298a322cbfbad)
- ref: 9f9b00d52ceafab6c183

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10566588306)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.10.4.md)
- [📈time plot](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.83%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.12.0.md)
- [📈time plot](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 67.18%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.13.0.md)
- [📈time plot](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.13.0b2.md)
- [📈time plot](bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d-vs-3.13.0b2.svg)

