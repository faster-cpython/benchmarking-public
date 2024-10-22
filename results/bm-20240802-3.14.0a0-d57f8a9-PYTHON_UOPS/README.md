# Results

- fork: python
- version: 3.14.0a0
- config: T2
- commit hash: [d57f8a9](https://github.com/python/cpython/commit/d57f8a9)
- commit date: 2024-08-02T09:09:27+03:00
- commit merge base: [5a7f7c48644baf82988f30bcb43e03dcfceb75dd](https://github.com/python/cpython/commit/5a7f7c48644baf82988f30bcb43e03dcfceb75dd)
- ref: main

## linux x86_64 (azure)

- [pystats raw](bm-20240802-azure-x86_64-python-main-3.14.0a0-d57f8a9-pystats.json)
- [pystats table](bm-20240802-azure-x86_64-python-main-3.14.0a0-d57f8a9-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10212928373)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.10.4.md)
- [📈time plot](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.12.0.md)
- [📈time plot](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.14x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.13.0.md)
- [📈time plot](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-linux-x86_64-python-main-3.14.0a0-d57f8a9-vs-3.13.0b2.svg)

