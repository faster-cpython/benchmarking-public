# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [b4d0d7d](https://github.com/python/cpython/commit/b4d0d7d)
- commit date: 2024-09-24T10:03:16-07:00
- commit merge base: [20ccda000b5f8365d5f864fd07876804157c2378](https://github.com/python/cpython/commit/20ccda000b5f8365d5f864fd07876804157c2378)
- ref: b4d0d7de0f6d938128bf

## linux x86_64 (azure)

- [pystats raw](bm-20240924-azure-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-pystats.json)
- [pystats table](bm-20240924-azure-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11057377176)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.10.4.md)
- [📈time plot](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.12.0.md)
- [📈time plot](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 99.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.13.0.md)
- [📈time plot](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.13.0b2.md)
- [📈time plot](bm-20240924-linux-x86_64-python-b4d0d7de0f6d938128bf-3.14.0a0-b4d0d7d-vs-3.13.0b2.svg)

