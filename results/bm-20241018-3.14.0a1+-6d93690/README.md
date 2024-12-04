# Results

- fork: python
- version: 3.14.0a1+
- config: 
- commit hash: [6d93690](https://github.com/python/cpython/commit/6d93690)
- commit date: 2024-10-18T09:26:08-06:00
- commit merge base: [2e950e341930ea79549137d4d3771d5edb940e65](https://github.com/python/cpython/commit/2e950e341930ea79549137d4d3771d5edb940e65)
- ref: 6d93690954daae9e9a36

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11409763599)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1%2B-6d93690.json)

### vs. 3.10.4

- Geometric mean: 1.412x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1%2B-6d93690-vs-3.10.4.md)
- [📈time plot](bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1%2B-6d93690-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1%2B-6d93690-vs-3.12.0.md)
- [📈time plot](bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1%2B-6d93690-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x faster (HPT: reliability of 96.70%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1%2B-6d93690-vs-3.13.0.md)
- [📈time plot](bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1%2B-6d93690-vs-3.13.0.svg)

