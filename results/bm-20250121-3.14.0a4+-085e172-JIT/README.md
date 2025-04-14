# Results

- fork: brandtbucher/remove_optimizer_api
- version: 3.14.0a4+
- config: JIT
- commit hash: [085e172](https://github.com/brandtbucher/cpython/commit/085e172)
- commit date: 2025-01-21T19:51:13-08:00
- commit merge base: [86c1a60d5a28cfb51f8843b307f8969c40e3bbec](https://github.com/python/cpython/commit/86c1a60d5a28cfb51f8843b307f8969c40e3bbec)
- ref: remove_optimizer_api

## linux x86_64 (azure)

- [pystats raw](bm-20250121-azure-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-pystats.json)
- [pystats table](bm-20250121-azure-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-pystats.md)

### vs. base

- [pystats diff](bm-20250121-azure-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12900853590)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172.json)

### vs. 3.10.4

- Geometric mean: 1.429x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-3.10.4.md)
- [📈time plot](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-3.12.0.md)
- [📈time plot](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 97.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-3.13.0.md)
- [📈time plot](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 95.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-base-mem.svg)
- [📄table](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-base.md)
- [📈time plot](bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4%2B-085e172-vs-base.svg)

