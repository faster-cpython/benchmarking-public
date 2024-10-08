# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [f88c14d](https://github.com/python/cpython/commit/f88c14d)
- commit date: 2024-08-20T20:10:15+03:00
- commit merge base: [bb1d30336e83837d4191a016107fd501cd230328](https://github.com/python/cpython/commit/bb1d30336e83837d4191a016107fd501cd230328)
- ref: f88c14d412522587085a

## linux x86_64 (azure)

- [pystats raw](bm-20240820-azure-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-pystats.json)
- [pystats table](bm-20240820-azure-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10495927347)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-vs-3.10.4.md)
- [📈time plot](bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-vs-3.12.0.md)
- [📈time plot](bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-vs-3.13.0b2.md)
- [📈time plot](bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d-vs-3.13.0b2.svg)

