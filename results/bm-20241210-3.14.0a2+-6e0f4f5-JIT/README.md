# Results

- fork: brandtbucher/justin_cold_20
- version: 3.14.0a2+
- config: JIT
- commit hash: [6e0f4f5](https://github.com/brandtbucher/cpython/commit/6e0f4f5)
- commit date: 2024-12-10T11:31:28-08:00
- commit merge base: [94b8f8b40943bf38cf5c454773a3fb8f4ff71e01](https://github.com/python/cpython/commit/94b8f8b40943bf38cf5c454773a3fb8f4ff71e01)
- ref: justin_cold_20

## linux x86_64 (azure)

- [pystats raw](bm-20241210-azure-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-pystats.json)
- [pystats table](bm-20241210-azure-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-pystats.md)

### vs. base

- [pystats diff](bm-20241210-azure-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12269867495)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5.json)

### vs. 3.10.4

- Geometric mean: 1.426x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-3.10.4.md)
- [📈time plot](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-3.12.0.md)
- [📈time plot](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-3.13.0.md)
- [📈time plot](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 73.74%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-base-mem.svg)
- [📄table](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-base.md)
- [📈time plot](bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2%2B-6e0f4f5-vs-base.svg)

