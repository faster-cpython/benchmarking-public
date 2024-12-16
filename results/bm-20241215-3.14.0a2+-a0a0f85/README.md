# Results

- fork: kumaraditya303/disable__asyncio
- version: 3.14.0a2+
- config: 
- commit hash: [a0a0f85](https://github.com/kumaraditya303/cpython/commit/a0a0f85)
- commit date: 2024-12-15T22:37:26+05:30
- commit merge base: [11ff3286b7e821bf439bc7caa0fa712e3bc3846a](https://github.com/python/cpython/commit/11ff3286b7e821bf439bc7caa0fa712e3bc3846a)
- ref: disable__asyncio

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356845204)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85.json)

### vs. 3.10.4

- Geometric mean: 1.389x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-3.10.4.md)
- [📈time plot](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-3.12.0.md)
- [📈time plot](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x slower (HPT: reliability of 69.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-3.13.0.md)
- [📈time plot](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.045x slower (HPT: reliability of 58.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-base-mem.svg)
- [📄table](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-base.md)
- [📈time plot](bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2%2B-a0a0f85-vs-base.svg)

