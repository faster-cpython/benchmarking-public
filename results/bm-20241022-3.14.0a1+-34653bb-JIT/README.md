# Results

- fork: python
- version: 3.14.0a1+
- config: JIT
- commit hash: [34653bb](https://github.com/python/cpython/commit/34653bb)
- commit date: 2024-10-22T13:42:22-07:00
- commit merge base: [aaed91cabcedc16c089c4b1c9abb1114659a83d3](https://github.com/python/cpython/commit/aaed91cabcedc16c089c4b1c9abb1114659a83d3)
- ref: 34653bba644aa5481613

## linux x86_64 (azure)

- [pystats raw](bm-20241022-azure-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-pystats.json)
- [pystats table](bm-20241022-azure-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11472492583)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)
- [📈time plot](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)
- [📈time plot](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x slower (HPT: reliability of 64.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)
- [📈time plot](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg)

