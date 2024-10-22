# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [1021191](https://github.com/mdboom/cpython/commit/1021191)
- commit date: 2024-08-29T11:26:16-04:00
- commit merge base: [58ce131037ecb34d506a613f21993cde2056f628](https://github.com/mdboom/cpython/commit/58ce131037ecb34d506a613f21993cde2056f628)
- ref: initialize_locals

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10618047876)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 94.37%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-base-mem.svg)
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-base.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191-vs-3.13.0b2.svg)

