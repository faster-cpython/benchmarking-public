# Results

- fork: python/703227dd021491ceb934
- version: 3.14.0a0
- config: 
- commit hash: [703227d](https://github.com/python/cpython/commit/703227d)
- commit date: 2024-10-15T10:51:37-04:00
- commit merge base: [d3c82b9ccedd77fc302f5ab8ab0220b3372f574c](https://github.com/python/cpython/commit/d3c82b9ccedd77fc302f5ab8ab0220b3372f574c)
- ref: 703227dd021491ceb934

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11362148418)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d.json)

### vs. 3.10.4

- Geometric mean: 1.399x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d-vs-3.10.4.md)
- [📈time plot](bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d-vs-3.12.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d-vs-3.13.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-703227dd021491ceb934-3.14.0a0-703227d-vs-3.13.0.svg)

