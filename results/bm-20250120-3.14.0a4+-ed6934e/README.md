# Results

- fork: python/ed6934e71e55d398df82
- version: 3.14.0a4+
- config: 
- commit hash: [ed6934e](https://github.com/python/cpython/commit/ed6934e)
- commit date: 2025-01-20T17:13:01+00:00
- commit merge base: [ab61d3f4303d14a413bc9ae6557c730ffdf7579e](https://github.com/python/cpython/commit/ab61d3f4303d14a413bc9ae6557c730ffdf7579e)
- ref: ed6934e71e55d398df82

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13121355001)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-3.10.4.md)
- [📈time plot](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.106x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-3.12.0.md)
- [📈time plot](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-3.13.0.md)
- [📈time plot](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 93.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-base-mem.svg)
- [📄table](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-base.md)
- [📈time plot](bm-20250120-linux-x86_64-python-ed6934e71e55d398df82-3.14.0a4%2B-ed6934e-vs-base.svg)

