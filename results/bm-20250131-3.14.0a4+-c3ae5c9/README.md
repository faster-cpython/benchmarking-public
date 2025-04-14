# Results

- fork: python/c3ae5c9e4ad121f8ba60
- version: 3.14.0a4+
- config: 
- commit hash: [c3ae5c9](https://github.com/python/cpython/commit/c3ae5c9)
- commit date: 2025-01-31T12:12:24+00:00
- commit merge base: [31c82c28f927b7e55c7dfdd548322c6c36760278](https://github.com/python/cpython/commit/31c82c28f927b7e55c7dfdd548322c6c36760278)
- ref: c3ae5c9e4ad121f8ba60

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13087833043)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4%2B-c3ae5c9.json)

### vs. 3.10.4

- Geometric mean: 1.365x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4%2B-c3ae5c9-vs-3.10.4.md)
- [📈time plot](bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4%2B-c3ae5c9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.056x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4%2B-c3ae5c9-vs-3.12.0.md)
- [📈time plot](bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4%2B-c3ae5c9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4%2B-c3ae5c9-vs-3.13.0.md)
- [📈time plot](bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4%2B-c3ae5c9-vs-3.13.0.svg)

