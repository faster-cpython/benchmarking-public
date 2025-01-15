# Results

- fork: brandtbucher/f2b86f10e60051aa48d5
- version: 3.14.0a4+
- config: JIT
- commit hash: [f2b86f1](https://github.com/brandtbucher/cpython/commit/f2b86f1)
- commit date: 2025-01-14T12:58:34-08:00
- commit merge base: [f7ceb317aec498823555885a4b7fed5e0244f300](https://github.com/python/cpython/commit/f7ceb317aec498823555885a4b7fed5e0244f300)
- ref: f2b86f10e60051aa48d5

## linux x86_64 (azure)

- [pystats raw](bm-20250114-azure-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-pystats.json)
- [pystats table](bm-20250114-azure-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-pystats.md)

### vs. base

- [pystats diff](bm-20250114-azure-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12778665544)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1.json)

### vs. 3.10.4

- Geometric mean: 1.426x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-3.10.4.md)
- [📈time plot](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.100x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-3.12.0.md)
- [📈time plot](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 97.16%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-3.13.0.md)
- [📈time plot](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 60.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-base-mem.svg)
- [📄table](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-base.md)
- [📈time plot](bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4%2B-f2b86f1-vs-base.svg)

