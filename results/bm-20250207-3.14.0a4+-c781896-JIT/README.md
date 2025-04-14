# Results

- fork: brandtbucher/no_underflow
- version: 3.14.0a4+
- config: JIT
- commit hash: [c781896](https://github.com/brandtbucher/cpython/commit/c781896)
- commit date: 2025-02-07T11:57:07-08:00
- commit merge base: [5fa7e1b7fd57e8c6297e9eb79d79cede42e5ce0f](https://github.com/python/cpython/commit/5fa7e1b7fd57e8c6297e9eb79d79cede42e5ce0f)
- ref: no_underflow

## linux x86_64 (azure)

- [pystats raw](bm-20250207-azure-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-pystats.json)
- [pystats table](bm-20250207-azure-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-pystats.md)

### vs. base

- [pystats diff](bm-20250207-azure-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13207089839)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896.json)

### vs. 3.10.4

- Geometric mean: 1.460x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-3.10.4.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-3.12.0.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-3.13.0.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-base-mem.svg)
- [📄table](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-base.md)
- [📈time plot](bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4%2B-c781896-vs-base.svg)

