# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [d27a53f](https://github.com/python/cpython/commit/d27a53f)
- commit date: 2024-07-30T11:53:07+03:00
- commit merge base: [3a9b2aae615165a40614db9aaa8b90c55ff0c7f9](https://github.com/python/cpython/commit/3a9b2aae615165a40614db9aaa8b90c55ff0c7f9)
- ref: d27a53fc02a87e76066f

## linux x86_64 (azure)

- [pystats raw](bm-20240730-azure-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-pystats.json)
- [pystats table](bm-20240730-azure-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10192972991)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.10.4.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.12.0.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 67.54%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.13.0.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 53.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- [🧠memory plot](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-base-mem.svg)
- [📄table](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-base.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.13.0b2.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f-vs-3.13.0b2.svg)

