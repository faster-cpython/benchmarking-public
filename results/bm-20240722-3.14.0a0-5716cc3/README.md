# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [5716cc3](https://github.com/python/cpython/commit/5716cc3)
- commit date: 2024-07-22T12:08:27-04:00
- commit merge base: [2408a8a22bd13d8f15172a2ecf8bbbc4355dcb3b](https://github.com/python/cpython/commit/2408a8a22bd13d8f15172a2ecf8bbbc4355dcb3b)
- ref: 5716cc352940a5f8557a

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10058635207)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.10.4.md)
- [📈time plot](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.12.0.md)
- [📈time plot](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.37%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.13.0.md)
- [📈time plot](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.13.0b2.md)
- [📈time plot](bm-20240722-linux-x86_64-python-5716cc352940a5f8557a-3.14.0a0-5716cc3-vs-3.13.0b2.svg)

