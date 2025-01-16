# Results

- fork: brandtbucher/justin_binary_op_swa
- version: 3.14.0a4+
- config: JIT
- commit hash: [6daa4a6](https://github.com/brandtbucher/cpython/commit/6daa4a6)
- commit date: 2025-01-15T17:51:09-08:00
- commit merge base: [f7ceb317aec498823555885a4b7fed5e0244f300](https://github.com/python/cpython/commit/f7ceb317aec498823555885a4b7fed5e0244f300)
- ref: justin_binary_op_swa

## linux x86_64 (azure)

- [pystats raw](bm-20250115-azure-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-pystats.json)
- [pystats table](bm-20250115-azure-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-pystats.md)

### vs. base

- [pystats diff](bm-20250115-azure-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12800535638)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6.json)

### vs. 3.10.4

- Geometric mean: 1.426x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.10.4.md)
- [📈time plot](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.12.0.md)
- [📈time plot](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 95.41%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.13.0.md)
- [📈time plot](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 99.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-base-mem.svg)
- [📄table](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-base.md)
- [📈time plot](bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4%2B-6daa4a6-vs-base.svg)

