# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [b5e142b](https://github.com/python/cpython/commit/b5e142b)
- commit date: 2024-08-06T23:31:39+00:00
- commit merge base: [4767a6e31c0550836b2af45d27e374e721f0c4e6](https://github.com/python/cpython/commit/4767a6e31c0550836b2af45d27e374e721f0c4e6)
- ref: b5e142ba7c2063efe9bb

## linux x86_64 (azure)

- [pystats raw](bm-20240806-azure-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-pystats.json)
- [pystats table](bm-20240806-azure-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10276289512)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-vs-3.10.4.md)
- [📈time plot](bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-vs-3.12.0.md)
- [📈time plot](bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-vs-3.13.0b2.md)
- [📈time plot](bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b-vs-3.13.0b2.svg)

