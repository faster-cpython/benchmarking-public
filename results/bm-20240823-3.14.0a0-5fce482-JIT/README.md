# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [5fce482](https://github.com/python/cpython/commit/5fce482)
- commit date: 2024-08-23T10:39:42+01:00
- commit merge base: [5d3201fe3f76aeba33e9e5956ba80a116e422bd0](https://github.com/python/cpython/commit/5d3201fe3f76aeba33e9e5956ba80a116e422bd0)
- ref: 5fce482c9a9d18d36c81

## linux x86_64 (azure)

- [pystats raw](bm-20240823-azure-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-pystats.json)
- [pystats table](bm-20240823-azure-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10567991229)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.10.4.md)
- [📈time plot](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.12.0.md)
- [📈time plot](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 83.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.13.0.md)
- [📈time plot](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.13.0b2.md)
- [📈time plot](bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482-vs-3.13.0b2.svg)

