# Results

- fork: python/d61542b5ff1fe64705e5
- version: 3.14.0a3+
- config: 
- commit hash: [d61542b](https://github.com/python/cpython/commit/d61542b)
- commit date: 2024-12-23T17:22:15+00:00
- commit merge base: [c5b0c90b62f1a10b0742db4bcd17da080d4e9111](https://github.com/python/cpython/commit/c5b0c90b62f1a10b0742db4bcd17da080d4e9111)
- ref: d61542b5ff1fe64705e5

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12550391505)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3%2B-d61542b.json)

### vs. 3.10.4

- Geometric mean: 1.339x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3%2B-d61542b-vs-3.10.4.md)
- [📈time plot](bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3%2B-d61542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3%2B-d61542b-vs-3.12.0.md)
- [📈time plot](bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3%2B-d61542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3%2B-d61542b-vs-3.13.0.md)
- [📈time plot](bm-20241223-pythonperf2-x86_64-python-d61542b5ff1fe64705e5-3.14.0a3%2B-d61542b-vs-3.13.0.svg)

