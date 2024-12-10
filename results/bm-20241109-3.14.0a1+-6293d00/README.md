# Results

- fork: python/6293d00e7201f3f28b1f
- version: 3.14.0a1+
- config: 
- commit hash: [6293d00](https://github.com/python/cpython/commit/6293d00)
- commit date: 2024-11-09T11:35:33+08:00
- commit merge base: [f8276bf5f37ef12aa0033634151fa33a6f7bd4f2](https://github.com/python/cpython/commit/f8276bf5f37ef12aa0033634151fa33a6f7bd4f2)
- ref: 6293d00e7201f3f28b1f

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11755880064)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00.json)

### vs. 3.10.4

- Geometric mean: 1.397x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.10.4.md)
- [📈time plot](bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.12.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 73.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.13.0.md)
- [📈time plot](bm-20241109-linux-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11897376333)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00.json)

### vs. 3.10.4

- Geometric mean: 1.311x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.10.4.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x faster (HPT: reliability of 92.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.12.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x faster (HPT: reliability of 99.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.13.0.md)
- [📈time plot](bm-20241109-pythonperf2-x86_64-python-6293d00e7201f3f28b1f-3.14.0a1%2B-6293d00-vs-3.13.0.svg)

