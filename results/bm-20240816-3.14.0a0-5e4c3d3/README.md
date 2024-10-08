# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [5e4c3d3](https://github.com/faster%2dcpython/cpython/commit/5e4c3d3)
- commit date: 2024-08-16T15:15:19+01:00
- commit merge base: [a07cf4ce25205d836a6b30cb629eda139d2a518e](https://github.com/faster%2dcpython/cpython/commit/a07cf4ce25205d836a6b30cb629eda139d2a518e)
- ref: specialize_shadowed_

## linux x86_64 (azure)

- [pystats raw](bm-20240816-azure-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-pystats.json)
- [pystats table](bm-20240816-azure-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-pystats.md)

### vs. base

- [pystats diff](bm-20240816-azure-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10421396792)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-3.10.4.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 81.01%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-3.12.0.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-3.13.0b2.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 58.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-base-mem.svg)
- [📄table](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-base.md)
- [📈time plot](bm-20240816-pythonperf2-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3-vs-base.svg)

