# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [d611c4c](https://github.com/python/cpython/commit/d611c4c)
- commit date: 2024-06-26T15:01:10-04:00
- commit merge base: [e51e880e75d79687b54a71351266e29ee349b4b8](https://github.com/python/cpython/commit/e51e880e75d79687b54a71351266e29ee349b4b8)
- ref: d611c4c8e9893c081696

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9713366731)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c.json)

### vs. 3.10.4

- Geometric mean: 1.20x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-3.10.4.md)
- [📈time plot](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.52x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-3.12.0.md)
- [📈time plot](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.60x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-3.13.0b2.md)
- [📈time plot](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.66x slower (HPT: reliability of 100.00%, 1.39x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-base-mem.svg)
- [📄table](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-base.md)
- [📈time plot](bm-20240626-linux-x86_64-python-d611c4c8e9893c081696-3.14.0a0-d611c4c-vs-base.svg)

