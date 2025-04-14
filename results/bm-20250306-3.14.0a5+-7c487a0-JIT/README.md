# Results

- fork: brandtbucher/jit_optimizer_truthy
- version: 3.14.0a5+
- config: JIT
- commit hash: [7c487a0](https://github.com/brandtbucher/cpython/commit/7c487a0)
- commit date: 2025-03-06T13:27:09-08:00
- commit merge base: [813bc5694bd8aa43165468c5ea1dc27af973611d](https://github.com/python/cpython/commit/813bc5694bd8aa43165468c5ea1dc27af973611d)
- ref: jit_optimizer_truthy

## linux x86_64 (azure)

- [pystats raw](bm-20250306-azure-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-pystats.json)
- [pystats table](bm-20250306-azure-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-pystats.md)

### vs. base

- [pystats diff](bm-20250306-azure-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13708700025)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0.json)

### vs. 3.10.4

- Geometric mean: 1.443x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-3.10.4.md)
- [📈time plot](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-3.12.0.md)
- [📈time plot](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-3.13.0.md)
- [📈time plot](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 99.39%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-base-mem.svg)
- [📄table](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-base.md)
- [📈time plot](bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5%2B-7c487a0-vs-base.svg)

