# Results

- fork: python/23f2e8f13c4e4a34106c
- version: 3.14.0a2+
- config: 
- commit hash: [23f2e8f](https://github.com/python/cpython/commit/23f2e8f)
- commit date: 2024-12-05T21:10:46+02:00
- commit merge base: [d958d9f4a1b71c6d30960bf6c53c41046ea94590](https://github.com/python/cpython/commit/d958d9f4a1b71c6d30960bf6c53c41046ea94590)
- ref: 23f2e8f13c4e4a34106c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12282375165)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241205-linux-x86_64-python-23f2e8f13c4e4a34106c-3.14.0a2%2B-23f2e8f.json)

### vs. 3.10.4

- Geometric mean: 1.421x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241205-linux-x86_64-python-23f2e8f13c4e4a34106c-3.14.0a2%2B-23f2e8f-vs-3.10.4.md)
- [📈time plot](bm-20241205-linux-x86_64-python-23f2e8f13c4e4a34106c-3.14.0a2%2B-23f2e8f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241205-linux-x86_64-python-23f2e8f13c4e4a34106c-3.14.0a2%2B-23f2e8f-vs-3.12.0.md)
- [📈time plot](bm-20241205-linux-x86_64-python-23f2e8f13c4e4a34106c-3.14.0a2%2B-23f2e8f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 99.16%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241205-linux-x86_64-python-23f2e8f13c4e4a34106c-3.14.0a2%2B-23f2e8f-vs-3.13.0.md)
- [📈time plot](bm-20241205-linux-x86_64-python-23f2e8f13c4e4a34106c-3.14.0a2%2B-23f2e8f-vs-3.13.0.svg)

