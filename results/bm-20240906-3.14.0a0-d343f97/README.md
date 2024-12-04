# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [d343f97](https://github.com/python/cpython/commit/d343f97)
- commit date: 2024-09-06T16:08:17+02:00
- commit merge base: [ef4b69d2becf49daaea21eb04effee81328a0393](https://github.com/python/cpython/commit/ef4b69d2becf49daaea21eb04effee81328a0393)
- ref: main

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10740414671)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97-vs-3.10.4.md)
- [📈time plot](bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97-vs-3.12.0.md)
- [📈time plot](bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97-vs-3.13.0.md)
- [📈time plot](bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97-vs-3.13.0.svg)

