# Results

- fork: python/813bc5694bd8aa431654
- version: 3.14.0a5+
- config: JIT
- commit hash: [813bc56](https://github.com/python/cpython/commit/813bc56)
- commit date: 2025-03-03T19:00:50-08:00
- commit merge base: [bbf197913ca984b79fee642a39bd61a997e24dd3](https://github.com/python/cpython/commit/bbf197913ca984b79fee642a39bd61a997e24dd3)
- ref: 813bc5694bd8aa431654

## linux x86_64 (azure)

- [pystats raw](bm-20250303-azure-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-pystats.json)
- [pystats table](bm-20250303-azure-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13661388801)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56.json)

### vs. 3.10.4

- Geometric mean: 1.441x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-vs-3.10.4.md)
- [📈time plot](bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-vs-3.12.0.md)
- [📈time plot](bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-vs-3.13.0.md)
- [📈time plot](bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5%2B-813bc56-vs-3.13.0.svg)

