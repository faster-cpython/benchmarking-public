# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [b0f4953](https://github.com/faster%2dcpython/cpython/commit/b0f4953)
- commit date: 2024-08-16T18:04:56+01:00
- commit merge base: [c13e7d98fb8581014a225b900b1b88ccbfc28097](https://github.com/faster%2dcpython/cpython/commit/c13e7d98fb8581014a225b900b1b88ccbfc28097)
- ref: specialize_shadowed_

## linux x86_64 (azure)

- [pystats raw](bm-20240816-azure-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-pystats.json)
- [pystats table](bm-20240816-azure-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-pystats.md)

### vs. base

- [pystats diff](bm-20240816-azure-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10424735319)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-3.10.4.md)
- [📈time plot](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-3.12.0.md)
- [📈time plot](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-3.13.0b2.md)
- [📈time plot](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 95.60%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-base-mem.svg)
- [📄table](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-base.md)
- [📈time plot](bm-20240816-linux-x86_64-faster%252dcpython-specialize_shadowed_-3.14.0a0-b0f4953-vs-base.svg)

