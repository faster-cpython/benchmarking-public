# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [5217328](https://github.com/python/cpython/commit/5217328)
- commit date: 2024-10-14T08:24:01+00:00
- commit merge base: [4b358ee647809019813f106eb901f466a3846d98](https://github.com/python/cpython/commit/4b358ee647809019813f106eb901f466a3846d98)
- ref: 5217328f93f599755bd7

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11325536521)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328.json)

### vs. 3.10.4

- Geometric mean: 1.398x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.10.4.md)
- [📈time plot](bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.12.0.md)
- [📈time plot](bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.13.0.md)
- [📈time plot](bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11325548685)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328.json)

### vs. 3.10.4

- Geometric mean: 1.137x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.10.4.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.12.0.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.13.0.md)
- [📈time plot](bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328-vs-3.13.0.svg)

