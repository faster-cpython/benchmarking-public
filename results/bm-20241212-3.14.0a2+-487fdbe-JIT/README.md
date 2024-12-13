# Results

- fork: python/487fdbed40734fd77214
- version: 3.14.0a2+
- config: JIT
- commit hash: [487fdbe](https://github.com/python/cpython/commit/487fdbe)
- commit date: 2024-12-12T11:22:20+00:00
- commit merge base: [292afd1d51dd7aacb12a6165f596ae7bb58c9ba8](https://github.com/python/cpython/commit/292afd1d51dd7aacb12a6165f596ae7bb58c9ba8)
- ref: 487fdbed40734fd77214

## linux x86_64 (azure)

- [pystats raw](bm-20241212-azure-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-pystats.json)
- [pystats table](bm-20241212-azure-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12305706643)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe.json)

### vs. 3.10.4

- Geometric mean: 1.427x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-vs-3.10.4.md)
- [📈time plot](bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-vs-3.12.0.md)
- [📈time plot](bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-vs-3.13.0.md)
- [📈time plot](bm-20241212-linux-x86_64-python-487fdbed40734fd77214-3.14.0a2%2B-487fdbe-vs-3.13.0.svg)

