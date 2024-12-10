# Results

- fork: python/7c2bd9b2266665ff4010
- version: 3.14.0a2+
- config: 
- commit hash: [7c2bd9b](https://github.com/python/cpython/commit/7c2bd9b)
- commit date: 2024-12-03T00:14:40+09:00
- commit merge base: [3e812253ab6b2f98fc5d17bfb82947e392b0b2a2](https://github.com/python/cpython/commit/3e812253ab6b2f98fc5d17bfb82947e392b0b2a2)
- ref: 7c2bd9b2266665ff4010

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12122901979)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2%2B-7c2bd9b.json)

### vs. 3.10.4

- Geometric mean: 1.431x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2%2B-7c2bd9b-vs-3.10.4.md)
- [📈time plot](bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2%2B-7c2bd9b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.097x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2%2B-7c2bd9b-vs-3.12.0.md)
- [📈time plot](bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2%2B-7c2bd9b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2%2B-7c2bd9b-vs-3.13.0.md)
- [📈time plot](bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2%2B-7c2bd9b-vs-3.13.0.svg)

