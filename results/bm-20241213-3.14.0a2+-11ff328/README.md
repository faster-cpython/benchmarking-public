# Results

- fork: python/11ff3286b7e821bf439b
- version: 3.14.0a2+
- config: 
- commit hash: [11ff328](https://github.com/python/cpython/commit/11ff328)
- commit date: 2024-12-13T14:57:02+05:30
- commit merge base: [58942a07df8811afba9c58dc16c1aab244ccf27a](https://github.com/python/cpython/commit/58942a07df8811afba9c58dc16c1aab244ccf27a)
- ref: 11ff3286b7e821bf439b

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12356845204)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2%2B-11ff328.json)

### vs. 3.10.4

- Geometric mean: 1.426x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2%2B-11ff328-vs-3.10.4.md)
- [📈time plot](bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2%2B-11ff328-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.096x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2%2B-11ff328-vs-3.12.0.md)
- [📈time plot](bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2%2B-11ff328-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2%2B-11ff328-vs-3.13.0.md)
- [📈time plot](bm-20241213-linux-x86_64-python-11ff3286b7e821bf439b-3.14.0a2%2B-11ff328-vs-3.13.0.svg)

