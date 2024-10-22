# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [23c2a0c](https://github.com/mdboom/cpython/commit/23c2a0c)
- commit date: 2024-08-29T11:16:14-04:00
- commit merge base: [58ce131037ecb34d506a613f21993cde2056f628](https://github.com/mdboom/cpython/commit/58ce131037ecb34d506a613f21993cde2056f628)
- ref: unicodekeys_compare_

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10617881657)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 92.28%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 97.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-base-mem.svg)
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-base.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c-vs-3.13.0b2.svg)

