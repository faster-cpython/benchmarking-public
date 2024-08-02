# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [db00fee](https://github.com/python/cpython/commit/db00fee)
- commit date: 2024-07-08T17:41:01+01:00
- commit merge base: [5289550b33de3d56f89a5d44a665283f7c8483a7](https://github.com/python/cpython/commit/5289550b33de3d56f89a5d44a665283f7c8483a7)
- ref: db00fee3a22db1c4b893

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9844334923)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee-vs-3.10.4.md)
- [📈time plot](bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee-vs-3.12.0.md)
- [📈time plot](bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee-vs-3.13.0b2.md)
- [📈time plot](bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee-vs-3.13.0b2.svg)

