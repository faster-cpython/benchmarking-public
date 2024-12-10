# Results

- fork: python/f8ba9fb2ce6690d2dd05
- version: 3.14.0a1+
- config: 
- commit hash: [f8ba9fb](https://github.com/python/cpython/commit/f8ba9fb)
- commit date: 2024-10-18T17:09:34+01:00
- commit merge base: [6d93690954daae9e9a368084765a4005f957686d](https://github.com/python/cpython/commit/6d93690954daae9e9a368084765a4005f957686d)
- ref: f8ba9fb2ce6690d2dd05

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11409763599)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb.json)

### vs. 3.10.4

- Geometric mean: 1.403x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-3.10.4.md)
- [📈time plot](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-3.12.0.md)
- [📈time plot](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 77.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-3.13.0.md)
- [📈time plot](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-base-mem.svg)
- [📄table](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-base.md)
- [📈time plot](bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1%2B-f8ba9fb-vs-base.svg)

