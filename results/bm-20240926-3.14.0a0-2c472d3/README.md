# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [2c472d3](https://github.com/python/cpython/commit/2c472d3)
- commit date: 2024-09-26T16:44:25+01:00
- commit merge base: [9c98fdab7d1167211c9d162c418e2b443a02867a](https://github.com/python/cpython/commit/9c98fdab7d1167211c9d162c418e2b443a02867a)
- ref: 2c472d36b776636fb008

## linux x86_64 (azure)

- [pystats raw](bm-20240926-azure-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-pystats.json)
- [pystats table](bm-20240926-azure-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11060807233)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.10.4.md)
- [📈time plot](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.12.0.md)
- [📈time plot](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 98.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.13.0.md)
- [📈time plot](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3-vs-3.13.0b2.svg)

