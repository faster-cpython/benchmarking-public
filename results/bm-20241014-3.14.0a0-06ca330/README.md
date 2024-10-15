# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [06ca330](https://github.com/python/cpython/commit/06ca330)
- commit date: 2024-10-14T14:18:57+01:00
- commit merge base: [67f6e08147bc005e460d82fcce85bf5d56009cf5](https://github.com/python/cpython/commit/67f6e08147bc005e460d82fcce85bf5d56009cf5)
- ref: 06ca33020e1168459fc6

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11351035494)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241014-linux-x86_64-python-06ca33020e1168459fc6-3.14.0a0-06ca330.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241014-linux-x86_64-python-06ca33020e1168459fc6-3.14.0a0-06ca330-vs-3.10.4.md)
- [📈time plot](bm-20241014-linux-x86_64-python-06ca33020e1168459fc6-3.14.0a0-06ca330-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-linux-x86_64-python-06ca33020e1168459fc6-3.14.0a0-06ca330-vs-3.12.0.md)
- [📈time plot](bm-20241014-linux-x86_64-python-06ca33020e1168459fc6-3.14.0a0-06ca330-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241014-linux-x86_64-python-06ca33020e1168459fc6-3.14.0a0-06ca330-vs-3.13.0b2.md)
- [📈time plot](bm-20241014-linux-x86_64-python-06ca33020e1168459fc6-3.14.0a0-06ca330-vs-3.13.0b2.svg)

