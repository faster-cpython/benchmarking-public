# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [c13e7d9](https://github.com/python/cpython/commit/c13e7d9)
- commit date: 2024-08-16T17:11:24+01:00
- commit merge base: [e2f2dc708eae89f41e328501b5ea7c97b8e39907](https://github.com/python/cpython/commit/e2f2dc708eae89f41e328501b5ea7c97b8e39907)
- ref: c13e7d98fb8581014a22

## linux x86_64 (azure)

- [pystats raw](bm-20240816-azure-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-pystats.json)
- [pystats table](bm-20240816-azure-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10424735319)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.10.4.md)
- [📈time plot](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.12.0.md)
- [📈time plot](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 77.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.13.0.md)
- [📈time plot](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.13.0b2.md)
- [📈time plot](bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9-vs-3.13.0b2.svg)

