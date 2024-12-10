# Results

- fork: python/2313f8421080ceb3343c
- version: 3.14.0a1+
- config: JIT
- commit hash: [2313f84](https://github.com/python/cpython/commit/2313f84)
- commit date: 2024-11-16T09:46:39+08:00
- commit merge base: [544b001b233ac57dfce17587ffbd10a70abe3ab0](https://github.com/python/cpython/commit/544b001b233ac57dfce17587ffbd10a70abe3ab0)
- ref: 2313f8421080ceb3343c

## linux x86_64 (azure)

- [pystats raw](bm-20241116-azure-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-pystats.json)
- [pystats table](bm-20241116-azure-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11883883618)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84.json)

### vs. 3.10.4

- Geometric mean: 1.385x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-3.10.4.md)
- [📈time plot](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.056x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-3.12.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x slower (HPT: reliability of 85.49%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-3.13.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 98.17%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-base-mem.svg)
- [📄table](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-base.md)
- [📈time plot](bm-20241116-linux-x86_64-python-2313f8421080ceb3343c-3.14.0a1%2B-2313f84-vs-base.svg)

