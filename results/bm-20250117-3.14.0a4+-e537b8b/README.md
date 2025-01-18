# Results

- fork: kumaraditya303/gc
- version: 3.14.0a4+
- config: 
- commit hash: [e537b8b](https://github.com/kumaraditya303/cpython/commit/e537b8b)
- commit date: 2025-01-17T19:55:09+00:00
- commit merge base: [d95ba9fa1110534b7247fa2ff12b90e930c93256](https://github.com/python/cpython/commit/d95ba9fa1110534b7247fa2ff12b90e930c93256)
- ref: gc

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12836101735)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b.json)

### vs. 3.10.4

- Geometric mean: 1.453x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.10.4.md)
- [📈time plot](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.12.0.md)
- [📈time plot](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.13.0.md)
- [📈time plot](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 56.34%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base-mem.svg)
- [📄table](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base.md)
- [📈time plot](bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4%2B-e537b8b-vs-base.svg)

