# Results

- fork: python/b2adf556747d080f04b5
- version: 3.14.0a3+
- config: 
- commit hash: [b2adf55](https://github.com/python/cpython/commit/b2adf55)
- commit date: 2025-01-09T15:40:45+05:30
- commit merge base: [1439b81928f1b52c5a0ac7fd81fdd66afd5f72da](https://github.com/python/cpython/commit/1439b81928f1b52c5a0ac7fd81fdd66afd5f72da)
- ref: b2adf556747d080f04b5

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12710290026)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3%2B-b2adf55.json)

### vs. 3.10.4

- Geometric mean: 1.445x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3%2B-b2adf55-vs-3.10.4.md)
- [📈time plot](bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3%2B-b2adf55-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3%2B-b2adf55-vs-3.12.0.md)
- [📈time plot](bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3%2B-b2adf55-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3%2B-b2adf55-vs-3.13.0.md)
- [📈time plot](bm-20250109-linux-x86_64-python-b2adf556747d080f04b5-3.14.0a3%2B-b2adf55-vs-3.13.0.svg)

