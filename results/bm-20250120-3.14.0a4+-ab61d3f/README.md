# Results

- fork: python/ab61d3f4303d14a413bc
- version: 3.14.0a4+
- config: 
- commit hash: [ab61d3f](https://github.com/python/cpython/commit/ab61d3f)
- commit date: 2025-01-20T17:09:23+00:00
- commit merge base: [0a6412f9cc9e694e76299cfbd73ec969b7d47af6](https://github.com/python/cpython/commit/0a6412f9cc9e694e76299cfbd73ec969b7d47af6)
- ref: ab61d3f4303d14a413bc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13121355001)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250120-linux-x86_64-python-ab61d3f4303d14a413bc-3.14.0a4%2B-ab61d3f.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250120-linux-x86_64-python-ab61d3f4303d14a413bc-3.14.0a4%2B-ab61d3f-vs-3.10.4.md)
- [📈time plot](bm-20250120-linux-x86_64-python-ab61d3f4303d14a413bc-3.14.0a4%2B-ab61d3f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250120-linux-x86_64-python-ab61d3f4303d14a413bc-3.14.0a4%2B-ab61d3f-vs-3.12.0.md)
- [📈time plot](bm-20250120-linux-x86_64-python-ab61d3f4303d14a413bc-3.14.0a4%2B-ab61d3f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250120-linux-x86_64-python-ab61d3f4303d14a413bc-3.14.0a4%2B-ab61d3f-vs-3.13.0.md)
- [📈time plot](bm-20250120-linux-x86_64-python-ab61d3f4303d14a413bc-3.14.0a4%2B-ab61d3f-vs-3.13.0.svg)

