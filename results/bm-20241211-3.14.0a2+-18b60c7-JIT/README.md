# Results

- fork: brandtbucher/justin_binary_op_swa
- version: 3.14.0a2+
- config: JIT
- commit hash: [18b60c7](https://github.com/brandtbucher/cpython/commit/18b60c7)
- commit date: 2024-12-11T19:10:25-08:00
- commit merge base: [94b8f8b40943bf38cf5c454773a3fb8f4ff71e01](https://github.com/python/cpython/commit/94b8f8b40943bf38cf5c454773a3fb8f4ff71e01)
- ref: justin_binary_op_swa

## linux x86_64 (azure)

- [pystats raw](bm-20241211-azure-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-pystats.json)
- [pystats table](bm-20241211-azure-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-pystats.md)

### vs. base

- [pystats diff](bm-20241211-azure-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12289086149)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7.json)

### vs. 3.10.4

- Geometric mean: 1.420x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-3.10.4.md)
- [📈time plot](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-3.12.0.md)
- [📈time plot](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 97.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-3.13.0.md)
- [📈time plot](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-base-mem.svg)
- [📄table](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-base.md)
- [📈time plot](bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2%2B-18b60c7-vs-base.svg)

