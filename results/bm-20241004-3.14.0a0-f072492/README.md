# Results

- fork: mdboom/marshal_slice
- version: 3.14.0a0
- config: 
- commit hash: [f072492](https://github.com/mdboom/cpython/commit/f072492)
- commit date: 2024-10-04T16:22:20-04:00
- commit merge base: [c8db0e817e7e0db501533fc8bf5b30c18e60aa3d](https://github.com/python/cpython/commit/c8db0e817e7e0db501533fc8bf5b30c18e60aa3d)
- ref: marshal_slice

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11186467973)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492.json)

### vs. 3.10.4

- Geometric mean: 1.432x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-3.10.4.md)
- [📈time plot](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-3.12.0.md)
- [📈time plot](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-3.13.0.md)
- [📈time plot](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 98.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-base-mem.svg)
- [📄table](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-base.md)
- [📈time plot](bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492-vs-base.svg)

