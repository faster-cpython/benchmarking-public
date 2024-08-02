# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [d1a1bca](https://github.com/python/cpython/commit/d1a1bca)
- commit date: 2024-07-30T14:03:52+02:00
- commit merge base: [d27a53fc02a87e76066fc4e15ff1fff3922a482d](https://github.com/python/cpython/commit/d27a53fc02a87e76066fc4e15ff1fff3922a482d)
- ref: d1a1bca1f0550a4715f1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10180691537)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-3.10.4.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-3.12.0.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-3.13.0b2.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-base-mem.svg)
- [📄table](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-base.md)
- [📈time plot](bm-20240730-linux-x86_64-python-d1a1bca1f0550a4715f1-3.14.0a0-d1a1bca-vs-base.svg)

