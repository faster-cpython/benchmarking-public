# Results

- fork: brandtbucher/warmup_side_2048
- version: 3.14.0a2+
- config: JIT
- commit hash: [7b551b8](https://github.com/brandtbucher/cpython/commit/7b551b8)
- commit date: 2024-11-21T12:38:58-08:00
- commit merge base: [0af4ec30bd2e3a52350344d1011c0c125d6dcd71](https://github.com/python/cpython/commit/0af4ec30bd2e3a52350344d1011c0c125d6dcd71)
- ref: warmup_side_2048

## linux x86_64 (azure)

- [pystats raw](bm-20241121-azure-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-pystats.json)
- [pystats table](bm-20241121-azure-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-pystats.md)

### vs. base

- [pystats diff](bm-20241121-azure-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11961414736)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8.json)

### vs. 3.10.4

- Geometric mean: 1.411x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-3.10.4.md)
- [📈time plot](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-3.12.0.md)
- [📈time plot](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x faster (HPT: reliability of 69.48%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-3.13.0.md)
- [📈time plot](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 73.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-base-mem.svg)
- [📄table](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-base.md)
- [📈time plot](bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2%2B-7b551b8-vs-base.svg)

