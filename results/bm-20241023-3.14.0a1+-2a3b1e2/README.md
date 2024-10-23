# Results

- fork: faster-cpython
- version: 3.14.0a1+
- config: 
- commit hash: [2a3b1e2](https://github.com/faster%2dcpython/cpython/commit/2a3b1e2)
- commit date: 2024-10-23T10:59:34+01:00
- commit merge base: [759a54d28ffe7eac8c23917f5d3dfad8309856be](https://github.com/faster%2dcpython/cpython/commit/759a54d28ffe7eac8c23917f5d3dfad8309856be)
- ref: load_const_return_re

## linux x86_64 (azure)

- [pystats raw](bm-20241023-azure-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-pystats.json)
- [pystats table](bm-20241023-azure-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-pystats.md)

### vs. base

- [pystats diff](bm-20241023-azure-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11477685504)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2.json)

### vs. 3.10.4

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-3.10.4.md)
- [📈time plot](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-3.12.0.md)
- [📈time plot](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 53.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: sphinx
- [📄table](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-3.13.0.md)
- [📈time plot](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 60.79%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-base-mem.svg)
- [📄table](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-base.md)
- [📈time plot](bm-20241023-linux-x86_64-faster%252dcpython-load_const_return_re-3.14.0a1%2B-2a3b1e2-vs-base.svg)

