# Results

- fork: python
- version: 3.14.0a1+
- config: 
- commit hash: [759a54d](https://github.com/python/cpython/commit/759a54d)
- commit date: 2024-10-22T10:57:25+00:00
- commit merge base: [57e3c59bb64fc2f8b2845a7e03ab0abb029ccd02](https://github.com/python/cpython/commit/57e3c59bb64fc2f8b2845a7e03ab0abb029ccd02)
- ref: 759a54d28ffe7eac8c23

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11475924205)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d.json)

### vs. 3.10.4

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.10.4.md)
- [📈time plot](bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.12.0.md)
- [📈time plot](bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 57.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.13.0.md)
- [📈time plot](bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1%2B-759a54d-vs-3.13.0.svg)

