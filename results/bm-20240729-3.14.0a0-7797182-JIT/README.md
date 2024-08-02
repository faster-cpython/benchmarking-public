# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [7797182](https://github.com/python/cpython/commit/7797182)
- commit date: 2024-07-29T14:49:17-07:00
- commit merge base: [78df1043dbdce5c989600616f9f87b4ee72944e5](https://github.com/python/cpython/commit/78df1043dbdce5c989600616f9f87b4ee72944e5)
- ref: 7797182b78baf78f64fe

## linux x86_64 (azure)

- [pystats raw](bm-20240729-azure-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-pystats.json)
- [pystats table](bm-20240729-azure-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10152951852)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-vs-3.10.4.md)
- [📈time plot](bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-vs-3.12.0.md)
- [📈time plot](bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-vs-3.13.0b2.md)
- [📈time plot](bm-20240729-linux-x86_64-python-7797182b78baf78f64fe-3.14.0a0-7797182-vs-3.13.0b2.svg)

